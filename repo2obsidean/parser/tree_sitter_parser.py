"""Tree-sitter based parser for Python and Go code."""

import re
import warnings
from pathlib import Path
from typing import Optional

# tree-sitter-languages ships grammars loaded via the older Language(path, name)
# API, which newer tree-sitter flags with a FutureWarning. It is harmless here.
warnings.filterwarnings("ignore", category=FutureWarning, module="tree_sitter")

import tree_sitter
import tree_sitter_languages

from repo2obsidean.parser.base import Language, Symbol, SymbolKind


class TreeSitterParser:
    """Parse Python and Go code using tree-sitter."""

    def __init__(self, language: Language = Language.PYTHON):
        self.language = language
        self.parser = self._load_parser(language)

    def _load_parser(self, language: Language) -> tree_sitter.Parser:
        """Load the tree-sitter parser for a language."""
        parser = tree_sitter.Parser()
        parser.set_language(tree_sitter_languages.get_language(language.value))
        return parser

    def parse_file(self, file_path: Path, layer: str = "") -> list[Symbol]:
        """Parse a file and extract symbols.

        ``layer`` labels which source root the file came from (e.g. "odoo",
        "user", "enterprise") and is stamped onto every returned symbol.
        """
        content_bytes = file_path.read_bytes()
        content_str = content_bytes.decode("utf-8", errors="replace")
        tree = self.parser.parse(content_bytes)
        lines = content_str.splitlines()

        symbols: list[Symbol] = []
        if self.language == Language.PYTHON:
            self._walk_python(tree.root_node, file_path, lines, symbols, scope_class=None)
        elif self.language == Language.GO:
            self._walk_go(tree.root_node, file_path, lines, symbols)
        elif self.language == Language.JAVASCRIPT:
            self._walk_js(tree.root_node, file_path, lines, symbols, scope_class=None)

        if layer:
            for s in symbols:
                s.layer = layer
        return symbols

    # ------------------------------------------------------------------ #
    # Python
    # ------------------------------------------------------------------ #

    def _walk_python(
        self,
        node: tree_sitter.Node,
        file_path: Path,
        lines: list[str],
        symbols: list[Symbol],
        scope_class: Optional[str],
        decorators: Optional[list[str]] = None,
    ):
        """Recursively walk the Python tree, emitting class/method/function symbols."""
        for child in node.children:
            if child.type == "decorated_definition":
                # Capture decorators, then process the wrapped definition.
                decs = self._python_decorators(child)
                self._walk_python(child, file_path, lines, symbols, scope_class, decs)

            elif child.type == "class_definition":
                name = self._field_text(child, "name")
                if not name:
                    continue
                odoo_model, odoo_inherit, odoo_inherits = self._python_odoo_attrs(child)
                symbols.append(
                    Symbol(
                        name=name,
                        kind=SymbolKind.CLASS,
                        language=Language.PYTHON,
                        qualified_name=name if scope_class is None else f"{scope_class}.{name}",
                        file=file_path,
                        start_line=child.start_point[0] + 1,
                        end_line=child.end_point[0] + 1,
                        signature=self._line_signature(child, lines),
                        docstring=self._python_docstring(child),
                        source_snippet=self._snippet(child, lines),
                        parents=self._python_base_classes(child),
                        decorators=decorators or [],
                        odoo_model=odoo_model,
                        odoo_inherit=odoo_inherit,
                        odoo_inherits=odoo_inherits,
                    )
                )
                # Recurse into the class body so methods get scope_class=name.
                body = child.child_by_field_name("body")
                if body is not None:
                    self._walk_python(body, file_path, lines, symbols, scope_class=name)

            elif child.type == "function_definition":
                name = self._field_text(child, "name")
                if not name:
                    continue
                if scope_class is not None:
                    kind = SymbolKind.METHOD
                    qualified = f"{scope_class}.{name}"
                    parents = [scope_class]
                else:
                    kind = SymbolKind.FUNCTION
                    qualified = name
                    parents = []
                symbols.append(
                    Symbol(
                        name=name,
                        kind=kind,
                        language=Language.PYTHON,
                        qualified_name=qualified,
                        file=file_path,
                        start_line=child.start_point[0] + 1,
                        end_line=child.end_point[0] + 1,
                        signature=self._line_signature(child, lines),
                        docstring=self._python_docstring(child),
                        source_snippet=self._snippet(child, lines),
                        parents=parents,
                        decorators=decorators or [],
                        calls=self._extract_calls(child),
                    )
                )
                # Do not descend into the function body for nested defs (MVP scope).

            else:
                self._walk_python(child, file_path, lines, symbols, scope_class)

    def _python_decorators(self, decorated_node: tree_sitter.Node) -> list[str]:
        """Extract decorator names from a decorated_definition node."""
        decorators = []
        for child in decorated_node.children:
            if child.type == "decorator":
                text = child.text.decode("utf-8").strip().lstrip("@").strip()
                decorators.append(text)
        return decorators

    def _python_base_classes(self, class_node: tree_sitter.Node) -> list[str]:
        """Extract base classes from a class_definition node."""
        bases = []
        superclasses = class_node.child_by_field_name("superclasses")
        if superclasses is not None:
            for child in superclasses.children:
                if child.type in ("identifier", "attribute"):
                    bases.append(child.text.decode("utf-8"))
        return bases

    def _python_odoo_attrs(
        self, class_node: tree_sitter.Node
    ) -> tuple[Optional[str], list[str], list[str]]:
        """Extract Odoo `_name`, `_inherit`, `_inherits` from a class body.

        These class-body assignments — not Python base classes — are how Odoo
        models relate to each other across addon trees.
        """
        model_name: Optional[str] = None
        inherit: list[str] = []
        inherits: list[str] = []

        body = class_node.child_by_field_name("body")
        if body is None:
            return model_name, inherit, inherits

        for stmt in body.children:
            if stmt.type != "expression_statement":
                continue
            for assign in stmt.children:
                if assign.type != "assignment":
                    continue
                left = assign.child_by_field_name("left")
                right = assign.child_by_field_name("right")
                if left is None or right is None:
                    continue
                key = left.text.decode("utf-8")
                if key == "_name":
                    model_name = self._str_value(right)
                elif key == "_inherit":
                    inherit = self._collect_strings(right)
                elif key == "_inherits":
                    inherits = self._dict_keys(right)

        return model_name, inherit, inherits

    def _str_value(self, node: tree_sitter.Node) -> Optional[str]:
        """Return the literal value of a string node, else None."""
        if node.type == "string":
            return self._strip_quotes(node.text.decode("utf-8"))
        return None

    def _collect_strings(self, node: tree_sitter.Node) -> list[str]:
        """Return string literal(s) from a string or a list-of-strings node."""
        if node.type == "string":
            return [self._strip_quotes(node.text.decode("utf-8"))]
        out = []
        if node.type in ("list", "tuple"):
            for child in node.children:
                if child.type == "string":
                    out.append(self._strip_quotes(child.text.decode("utf-8")))
        return out

    def _dict_keys(self, node: tree_sitter.Node) -> list[str]:
        """Return the string keys of a dictionary node (Odoo `_inherits`)."""
        out = []
        if node.type == "dictionary":
            for pair in node.children:
                if pair.type == "pair":
                    key = pair.child_by_field_name("key")
                    if key is not None and key.type == "string":
                        out.append(self._strip_quotes(key.text.decode("utf-8")))
        return out

    def _strip_quotes(self, raw: str) -> str:
        """Strip surrounding quotes/prefixes from a Python string literal."""
        text = raw.strip()
        text = re.sub(r'^[rbfuRBFU]*("""|\'\'\'|"|\')', "", text)
        text = re.sub(r'("""|\'\'\'|"|\')$', "", text)
        return text.strip()

    def _python_docstring(self, def_node: tree_sitter.Node) -> str:
        """Extract the docstring (first string literal in the body)."""
        body = def_node.child_by_field_name("body")
        if body is None:
            return ""
        for stmt in body.children:
            if stmt.type == "expression_statement":
                for expr in stmt.children:
                    if expr.type == "string":
                        raw = expr.text.decode("utf-8")
                        return self._clean_docstring(raw)
            # Only the first statement can be a docstring.
            if stmt.type not in ("comment",):
                break
        return ""

    # ------------------------------------------------------------------ #
    # Go
    # ------------------------------------------------------------------ #

    def _walk_go(
        self,
        node: tree_sitter.Node,
        file_path: Path,
        lines: list[str],
        symbols: list[Symbol],
    ):
        """Recursively walk the Go tree, emitting type/func/method symbols."""
        for child in node.children:
            if child.type == "type_declaration":
                for spec in child.children:
                    if spec.type == "type_spec":
                        name = self._field_text(spec, "name")
                        if name:
                            symbols.append(
                                Symbol(
                                    name=name,
                                    kind=SymbolKind.CLASS,  # struct/interface ~ class
                                    language=Language.GO,
                                    qualified_name=name,
                                    file=file_path,
                                    start_line=spec.start_point[0] + 1,
                                    end_line=spec.end_point[0] + 1,
                                    signature=self._line_signature(spec, lines),
                                    docstring=self._go_doc_comment(child, lines),
                                    source_snippet=self._snippet(spec, lines),
                                )
                            )

            elif child.type == "function_declaration":
                name = self._field_text(child, "name")
                if name:
                    symbols.append(
                        Symbol(
                            name=name,
                            kind=SymbolKind.FUNCTION,
                            language=Language.GO,
                            qualified_name=name,
                            file=file_path,
                            start_line=child.start_point[0] + 1,
                            end_line=child.end_point[0] + 1,
                            signature=self._line_signature(child, lines),
                            docstring=self._go_doc_comment(child, lines),
                            source_snippet=self._snippet(child, lines),
                            calls=self._extract_calls(child),
                        )
                    )

            elif child.type == "method_declaration":
                name = self._field_text(child, "name")
                receiver = self._go_receiver(child)
                if name:
                    symbols.append(
                        Symbol(
                            name=name,
                            kind=SymbolKind.METHOD,
                            language=Language.GO,
                            qualified_name=f"{receiver}.{name}" if receiver else name,
                            file=file_path,
                            start_line=child.start_point[0] + 1,
                            end_line=child.end_point[0] + 1,
                            signature=self._line_signature(child, lines),
                            docstring=self._go_doc_comment(child, lines),
                            source_snippet=self._snippet(child, lines),
                            parents=[receiver] if receiver else [],
                            calls=self._extract_calls(child),
                        )
                    )
            else:
                self._walk_go(child, file_path, lines, symbols)

    def _go_receiver(self, method_node: tree_sitter.Node) -> Optional[str]:
        """Extract the receiver type of a Go method (e.g. '*Service' -> 'Service')."""
        receiver = method_node.child_by_field_name("receiver")
        if receiver is None:
            return None
        for param in receiver.children:
            if param.type == "parameter_declaration":
                type_node = param.child_by_field_name("type")
                if type_node is not None:
                    return type_node.text.decode("utf-8").lstrip("*")
        return None

    def _go_doc_comment(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Extract the leading // comment block above a Go declaration."""
        start = node.start_point[0]
        doc_lines = []
        i = start - 1
        while i >= 0:
            stripped = lines[i].strip()
            if stripped.startswith("//"):
                doc_lines.insert(0, stripped[2:].strip())
                i -= 1
            else:
                break
        return " ".join(doc_lines)[:500]

    # ------------------------------------------------------------------ #
    # JavaScript
    # ------------------------------------------------------------------ #

    def _walk_js(
        self,
        node: tree_sitter.Node,
        file_path: Path,
        lines: list[str],
        symbols: list[Symbol],
        scope_class: Optional[str],
    ):
        """Recursively walk the JS tree, emitting class/method/function symbols."""
        for child in node.children:
            if child.type in ("class_declaration", "class"):
                name = self._field_text(child, "name") or "<anonymous>"
                symbols.append(
                    Symbol(
                        name=name,
                        kind=SymbolKind.CLASS,
                        language=Language.JAVASCRIPT,
                        qualified_name=name,
                        file=file_path,
                        start_line=child.start_point[0] + 1,
                        end_line=child.end_point[0] + 1,
                        signature=self._line_signature(child, lines),
                        docstring=self._js_doc_comment(child, lines),
                        source_snippet=self._snippet(child, lines),
                        parents=self._js_heritage(child),
                    )
                )
                body = child.child_by_field_name("body")
                if body is not None:
                    self._walk_js(body, file_path, lines, symbols, scope_class=name)

            elif child.type == "method_definition" and scope_class is not None:
                name = self._field_text(child, "name") or "<anonymous>"
                symbols.append(
                    Symbol(
                        name=name,
                        kind=SymbolKind.METHOD,
                        language=Language.JAVASCRIPT,
                        qualified_name=f"{scope_class}.{name}",
                        file=file_path,
                        start_line=child.start_point[0] + 1,
                        end_line=child.end_point[0] + 1,
                        signature=self._line_signature(child, lines),
                        docstring=self._js_doc_comment(child, lines),
                        source_snippet=self._snippet(child, lines),
                        parents=[scope_class],
                        calls=self._extract_calls(child),
                    )
                )

            elif child.type == "function_declaration":
                name = self._field_text(child, "name")
                if name:
                    symbols.append(
                        Symbol(
                            name=name,
                            kind=SymbolKind.FUNCTION,
                            language=Language.JAVASCRIPT,
                            qualified_name=name,
                            file=file_path,
                            start_line=child.start_point[0] + 1,
                            end_line=child.end_point[0] + 1,
                            signature=self._line_signature(child, lines),
                            docstring=self._js_doc_comment(child, lines),
                            source_snippet=self._snippet(child, lines),
                            calls=self._extract_calls(child),
                        )
                    )

            elif child.type in ("lexical_declaration", "variable_declaration"):
                # const foo = () => {} / const bar = function () {}
                for decl in child.children:
                    if decl.type != "variable_declarator":
                        continue
                    value = decl.child_by_field_name("value")
                    if value is None or value.type not in (
                        "arrow_function", "function", "function_expression",
                    ):
                        continue
                    name = self._field_text(decl, "name")
                    if name:
                        symbols.append(
                            Symbol(
                                name=name,
                                kind=SymbolKind.FUNCTION,
                                language=Language.JAVASCRIPT,
                                qualified_name=name,
                                file=file_path,
                                start_line=decl.start_point[0] + 1,
                                end_line=decl.end_point[0] + 1,
                                signature=self._line_signature(decl, lines),
                                docstring=self._js_doc_comment(child, lines),
                                source_snippet=self._snippet(decl, lines),
                                calls=self._extract_calls(value),
                            )
                        )
            else:
                self._walk_js(child, file_path, lines, symbols, scope_class)

    def _js_heritage(self, class_node: tree_sitter.Node) -> list[str]:
        """Extract the superclass from a JS `class X extends Y` declaration."""
        bases = []
        for child in class_node.children:
            if child.type == "class_heritage":
                for sub in child.children:
                    if sub.type in ("identifier", "member_expression"):
                        bases.append(sub.text.decode("utf-8"))
        return bases

    def _js_doc_comment(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Extract a leading // or /** */ comment block above a JS declaration."""
        start = node.start_point[0]
        doc_lines = []
        i = start - 1
        while i >= 0:
            stripped = lines[i].strip()
            if not stripped:
                i -= 1
                continue
            if stripped.startswith(("//", "/*", "*", "*/")):
                cleaned = stripped.lstrip("/*").rstrip("*/").strip()
                if cleaned:
                    doc_lines.insert(0, cleaned)
                i -= 1
            else:
                break
        return " ".join(doc_lines)[:500]

    # ------------------------------------------------------------------ #
    # Shared helpers
    # ------------------------------------------------------------------ #

    def _field_text(self, node: tree_sitter.Node, field: str) -> Optional[str]:
        """Get the decoded text of a named field child."""
        child = node.child_by_field_name(field)
        if child is not None:
            return child.text.decode("utf-8")
        return None

    def _line_signature(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Build a one-line signature up to the opening brace/colon."""
        start = node.start_point[0]
        collected = []
        for i in range(start, min(start + 8, len(lines))):
            collected.append(lines[i])
            if ":" in lines[i] or "{" in lines[i]:
                break
        sig = " ".join(collected).strip()
        # Trim everything after the first body-opener.
        for opener in (":", "{"):
            idx = sig.find(opener)
            if idx != -1:
                sig = sig[:idx]
        return re.sub(r"\s+", " ", sig).strip()[:200]

    def _snippet(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Get a capped source snippet for a node."""
        start = node.start_point[0]
        end = min(node.end_point[0] + 1, len(lines))
        return "\n".join(lines[start:end])[:800]

    def _clean_docstring(self, raw: str) -> str:
        """Strip quotes/prefixes from a Python string literal docstring."""
        text = raw.strip()
        text = re.sub(r'^[rbfRBF]*("""|\'\'\'|"|\')', "", text)
        text = re.sub(r'("""|\'\'\'|"|\')$', "", text)
        return text.strip()[:500]

    def _extract_calls(self, node: tree_sitter.Node) -> list[str]:
        """Extract called function/method names within a node's subtree."""
        calls: list[str] = []
        self._walk_calls(node, calls)
        # Preserve order, dedupe.
        seen = set()
        result = []
        for c in calls:
            if c not in seen:
                seen.add(c)
                result.append(c)
        return result

    def _walk_calls(self, node: tree_sitter.Node, calls: list[str]):
        """Recursively collect call target names."""
        if node.type in ("call", "call_expression"):
            fn = node.child_by_field_name("function")
            if fn is not None:
                if fn.type == "identifier":
                    calls.append(fn.text.decode("utf-8"))
                elif fn.type in ("attribute", "selector_expression"):
                    text = fn.text.decode("utf-8")
                    calls.append(text.split(".")[-1])
        for child in node.children:
            self._walk_calls(child, calls)
