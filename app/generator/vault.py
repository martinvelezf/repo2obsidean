"""Generate Obsidian vault from symbol graph."""

import shutil
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

from app.graph.builder import SymbolGraph
from app.generator.slug import slug_from_symbol, wikilink_from_qualified_name, normalize_call_target
from app.parser.base import Symbol, SymbolKind


class VaultGenerator:
    """Generate an Obsidian vault from a symbol graph."""

    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.notes_dir = self.output_dir / "Notes"
        self.env = self._setup_jinja()

    def _setup_jinja(self) -> Environment:
        """Set up Jinja2 environment.

        Autoescape is OFF: we emit Markdown, not HTML, so escaping quotes/angle
        brackets in source snippets would corrupt the output.
        """
        template_dir = Path(__file__).parent / "templates"
        return Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def generate(self, graph: SymbolGraph):
        """Generate the vault from a symbol graph.

        Only the generated ``Notes/`` content is wiped and rebuilt. Anything
        else in the output directory — notably Obsidian's own ``.obsidian/``
        config (graph color groups, workspace, appearance) — is preserved, so
        regenerating doesn't blow away the user's graph setup.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if self.notes_dir.exists():
            shutil.rmtree(self.notes_dir)
        self.notes_dir.mkdir(parents=True)

        # Iterate the full list (not the deduped dict) so identically-named
        # classes across files/layers each get their own note.
        self._written_paths: set[Path] = set()
        for symbol in graph.all_symbols:
            self._generate_note(symbol, graph)

        # Index + MOCs use the deduped dict (one entry per qualified name).
        symbols = graph.export_symbols()
        self._generate_index(symbols)
        self._generate_mocs(symbols, graph)

        # Framework-aware report: Odoo model inheritance across layers.
        self._generate_odoo_report(graph)

        # Git: index of symbols changed since HEAD.
        self._generate_recent_changes(graph)

    def _generate_note(self, symbol: Symbol, graph: SymbolGraph):
        """Generate a markdown note for a symbol."""
        # slug already includes the "Notes/" prefix, so join to output_dir.
        slug = slug_from_symbol(symbol)
        note_path = self.output_dir / slug
        note_path = self._unique_path(note_path)
        note_path.parent.mkdir(parents=True, exist_ok=True)

        # Prepare context for template
        callers = graph.get_callers(symbol.qualified_name)
        callees = graph.get_callees(symbol.qualified_name)

        context = {
            "symbol": symbol,
            "callers": self._format_links(callers),
            "callees": self._format_links(callees),
            "related": self._format_links(graph.get_related_symbols(symbol.qualified_name)),
            "aliases": [symbol.qualified_name, symbol.name],
            # Odoo metadata (empty/None for non-Odoo code -> templates skip it).
            "odoo_model": symbol.odoo_model,
            "odoo_inherit": symbol.odoo_inherit,
            "odoo_inherits": symbol.odoo_inherits,
            # Git change metadata.
            "changed": symbol.changed,
            "change_status": symbol.change_status,
            "change_diff": symbol.change_diff,
        }

        # Choose template based on symbol kind
        if symbol.kind == SymbolKind.CLASS:
            template = self.env.get_template("class.md.j2")
        elif symbol.kind == SymbolKind.METHOD:
            template = self.env.get_template("method.md.j2")
        elif symbol.kind == SymbolKind.FUNCTION:
            template = self.env.get_template("function.md.j2")
        else:
            template = self.env.get_template("function.md.j2")

        content = template.render(**context)
        note_path.write_text(content, encoding="utf-8")

    def _unique_path(self, path: Path) -> Path:
        """Return a non-colliding path, appending -2, -3, ... if needed."""
        if path not in self._written_paths:
            self._written_paths.add(path)
            return path
        stem, suffix = path.stem, path.suffix
        i = 2
        while True:
            candidate = path.with_name(f"{stem}-{i}{suffix}")
            if candidate not in self._written_paths:
                self._written_paths.add(candidate)
                return candidate
            i += 1

    def _generate_odoo_report(self, graph: SymbolGraph):
        """Write an Odoo model-inheritance report, including the dangling check.

        Skipped entirely when the codebase has no Odoo models.
        """
        if not graph.odoo_models:
            return

        lines = ["# Odoo Model Inheritance", ""]

        unresolved = graph.odoo_unresolved
        if unresolved:
            lines.append("## ⚠️ Unresolved inherits")
            lines.append("")
            lines.append("Models referenced via `_inherit`/`_inherits` but **never "
                         "defined** in the scanned roots (likely a missing addon tree):")
            lines.append("")
            for model in sorted(unresolved):
                referrers = unresolved[model]
                layers = sorted({s.layer or "?" for s in referrers})
                lines.append(f"- `{model}` — referenced by {len(referrers)} class(es) "
                             f"in layer(s): {', '.join(layers)}")
            lines.append("")

        lines.append("## Models")
        lines.append("")
        for model in sorted(graph.odoo_models):
            info = graph.odoo_models[model]
            bases, exts = info["bases"], info["extensions"]
            status = "✅" if bases else "⚠️ no base definition"
            lines.append(f"### `{model}` {status}")
            lines.append("")
            if bases:
                lines.append("**Defined in:**")
                for s in bases:
                    lines.append(f"- [{s.layer or 'root'}] `{s.file}` "
                                 f"→ class `{s.name}` (line {s.start_line})")
            if exts:
                lines.append("")
                lines.append("**Extended in:**")
                for s in exts:
                    lines.append(f"- [{s.layer or 'root'}] `{s.file}` "
                                 f"→ class `{s.name}` (line {s.start_line})")
            lines.append("")

        (self.notes_dir / "odoo-models.md").write_text("\n".join(lines), encoding="utf-8")

    def _symbol_link(self, symbol: Symbol) -> str:
        """Wikilink text matching the symbol's note filename (sans .md)."""
        if symbol.kind == SymbolKind.METHOD and symbol.parents:
            return f"{symbol.parents[0]}__{symbol.name}"
        return symbol.name

    def _generate_recent_changes(self, graph: SymbolGraph):
        """Write an index of symbols whose source changed since git HEAD."""
        changed = [s for s in graph.all_symbols if s.changed]
        if not changed:
            return

        status_label = {"M": "modified", "A": "added", "D": "deleted"}
        lines = [
            "---",
            "tags: [obsidean, recent-changes]",
            "---",
            "",
            "# Recent Changes",
            "",
            f"{len(changed)} symbol(s) changed in the working tree since git HEAD.",
            "",
        ]

        # Group by layer, then by file.
        by_layer: dict[str, dict[str, list[Symbol]]] = {}
        for s in changed:
            by_layer.setdefault(s.layer or "root", {}).setdefault(str(s.file), []).append(s)

        for layer in sorted(by_layer):
            lines.append(f"## {layer}")
            lines.append("")
            for file in sorted(by_layer[layer]):
                lines.append(f"**`{file}`**")
                lines.append("")
                for s in sorted(by_layer[layer][file], key=lambda x: x.start_line):
                    label = status_label.get(s.change_status, s.change_status or "changed")
                    lines.append(f"- [[{self._symbol_link(s)}]] "
                                 f"— {s.kind.value} ({label}, line {s.start_line})")
                lines.append("")

        (self.notes_dir / "recent-changes.md").write_text("\n".join(lines), encoding="utf-8")

    def _format_links(self, qualified_names: list[str]) -> str:
        """Format a list of qualified names as Obsidian wikilinks."""
        if not qualified_names:
            return ""

        lines = []
        for qname in sorted(set(qualified_names)):
            if not qname.startswith("?"):
                # Extract the last component for the link text
                parts = qname.split(".")
                link_text = f"{parts[-2]}__{parts[-1]}" if len(parts) >= 2 and parts[-2][0].isupper() else parts[-1]
                lines.append(f"- [[{link_text}]]")

        return "\n".join(lines) if lines else "_none_"

    def _generate_index(self, symbols: dict[str, Symbol]):
        """Generate the index.md file."""
        index_path = self.notes_dir / "index.md"

        # Group symbols by language
        by_language = {}
        for qname, symbol in symbols.items():
            lang = symbol.language.value
            if lang not in by_language:
                by_language[lang] = []
            by_language[lang].append(symbol)

        content = "# Codebase Index\n\n"
        for lang in sorted(by_language.keys()):
            content += f"## {lang.capitalize()}\n\n"
            # Group by module
            by_module = {}
            for symbol in by_language[lang]:
                parts = symbol.qualified_name.split(".")
                module = ".".join(parts[:-1]) if len(parts) > 1 else "_root_"
                if module not in by_module:
                    by_module[module] = []
                by_module[module].append(symbol)

            for module in sorted(by_module.keys()):
                content += f"### {module}\n\n"
                for symbol in sorted(by_module[module], key=lambda s: s.name):
                    slug = slug_from_symbol(symbol)
                    relative_link = slug.relative_to("Notes")
                    content += f"- [[{symbol.qualified_name}|{symbol.name}]] (`{symbol.kind.value}`)\n"

                content += "\n"

        index_path.write_text(content, encoding="utf-8")

    def _generate_mocs(self, symbols: dict[str, Symbol], graph: SymbolGraph):
        """Generate Maps of Content for each language and module."""
        # Group by language
        by_language = {}
        for qname, symbol in symbols.items():
            lang = symbol.language.value
            if lang not in by_language:
                by_language[lang] = []
            by_language[lang].append(symbol)

        # Generate language-level MOC
        for lang in by_language.keys():
            moc_path = self.notes_dir / f"MOC-{lang}.md"
            content = f"# {lang.capitalize()} Symbols\n\n"

            by_module = {}
            for symbol in by_language[lang]:
                parts = symbol.qualified_name.split(".")
                module = ".".join(parts[:-1]) if len(parts) > 1 else "_root_"
                if module not in by_module:
                    by_module[module] = []
                by_module[module].append(symbol)

            for module in sorted(by_module.keys()):
                content += f"## {module}\n\n"
                for symbol in sorted(by_module[module], key=lambda s: s.name):
                    if symbol.kind == SymbolKind.CLASS:
                        content += f"- [[{symbol.qualified_name}|{symbol.name}]] (class)\n"
                        # List methods under the class
                        for qname, other in symbols.items():
                            if other.kind == SymbolKind.METHOD and other.parents and other.parents[0] == symbol.name:
                                method_slug = slug_from_symbol(other)
                                content += f"  - [[{other.qualified_name}|{other.name}]]\n"
                    elif symbol.kind == SymbolKind.FUNCTION:
                        content += f"- [[{symbol.qualified_name}|{symbol.name}]] (function)\n"

                content += "\n"

            moc_path.write_text(content, encoding="utf-8")
