"""Build a symbol graph from parsed symbols."""

from pathlib import Path
from typing import Optional

import networkx as nx

from app.parser.base import Symbol, SymbolKind


class SymbolGraph:
    """A directed graph of code symbols and their relationships."""

    def __init__(self):
        self.graph = nx.DiGraph()
        self.symbols: dict[str, Symbol] = {}
        # Full, un-deduplicated symbol list (identically-named classes across
        # layers all survive here, unlike the qualified_name-keyed dict above).
        self.all_symbols: list[Symbol] = []
        # Odoo model name -> {"bases": [...], "extensions": [...]}
        self.odoo_models: dict[str, dict] = {}
        # Model names referenced via _inherit/_inherits with no base definition.
        self.odoo_unresolved: dict[str, list[Symbol]] = {}

    def add_symbol(self, symbol: Symbol):
        """Add a symbol to the graph."""
        self.symbols[symbol.qualified_name] = symbol
        self.graph.add_node(
            symbol.qualified_name,
            kind=symbol.kind,
            language=symbol.language,
            file=symbol.file,
            line=symbol.start_line,
        )

    def add_edge(self, source: str, target: str, edge_type: str):
        """Add an edge between two symbols."""
        self.graph.add_edge(source, target, type=edge_type)

    def build_from_symbols(self, symbols: list[Symbol]):
        """Build the graph from a list of parsed symbols."""
        self.all_symbols = list(symbols)

        # Add all symbols as nodes
        for symbol in symbols:
            self.add_symbol(symbol)

        # Build relationships
        for symbol in symbols:
            # Parent relationships (inheritance)
            for parent in symbol.parents:
                # Try to resolve parent in same module
                parent_qualified = self._resolve_name(parent, symbol.qualified_name)
                if parent_qualified in self.symbols:
                    self.add_edge(symbol.qualified_name, parent_qualified, "INHERITS")

            # Call relationships
            for call in symbol.calls:
                call_qualified = self._resolve_call(call, symbol)
                if call_qualified in self.symbols:
                    self.add_edge(symbol.qualified_name, call_qualified, "CALLS")
                else:
                    # Add as unresolved node for later reference
                    self.graph.add_node(call_qualified, unresolved=True)
                    self.add_edge(symbol.qualified_name, call_qualified, "CALLS")

            # Import relationships
            for imp in symbol.imports:
                if imp in self.symbols:
                    self.add_edge(symbol.qualified_name, imp, "IMPORTS")

        # Framework-aware: link Odoo models across layers by model name.
        self._build_odoo_index(symbols)

    def _build_odoo_index(self, symbols: list[Symbol]):
        """Index Odoo models by name and link definitions to extensions.

        This is framework-specific (Odoo) but harmless for any other codebase:
        if no class declares `_name`/`_inherit`, the index is simply empty.

        A class is a *base* of model M when it sets `_name = M` (optionally with
        `_inherit = M`). A class is an *extension* of M when it sets
        `_inherit = M` (or lists M) without redefining `_name`. Mixins pulled in
        via `_inherit`/`_inherits` are also recorded as references to M.
        """
        models: dict[str, dict] = {}

        def slot(model: str) -> dict:
            return models.setdefault(model, {"bases": [], "extensions": [], "refs": []})

        for s in symbols:
            if s.kind != SymbolKind.CLASS:
                continue
            if not (s.odoo_model or s.odoo_inherit or s.odoo_inherits):
                continue

            if s.odoo_model:
                # Declares a model identity -> it is a base definition.
                slot(s.odoo_model)["bases"].append(s)
                # If it also _inherits other models (prototype/mixin), record refs.
                for m in s.odoo_inherit:
                    if m != s.odoo_model:
                        slot(m)["refs"].append(s)
            else:
                # No _name: it extends each model it inherits in place.
                for m in s.odoo_inherit:
                    slot(m)["extensions"].append(s)

            # Delegation inheritance always references the delegated models.
            for m in s.odoo_inherits:
                slot(m)["refs"].append(s)

        self.odoo_models = models

        # A model referenced (extended/delegated) but never defined is dangling.
        self.odoo_unresolved = {
            name: info["extensions"] + info["refs"]
            for name, info in models.items()
            if not info["bases"]
        }

        # Wire INHERITS edges between extension classes and base definitions so
        # the relationship shows up in the graph and per-note backlinks.
        for name, info in models.items():
            for base in info["bases"]:
                for ext in info["extensions"]:
                    if ext.qualified_name in self.graph and base.qualified_name in self.graph:
                        self.add_edge(ext.qualified_name, base.qualified_name, "INHERITS")

    def _resolve_name(self, name: str, context: str) -> str:
        """Resolve a name in the given context."""
        # If it's already qualified, return as-is
        if "." in name:
            return name

        # Try to resolve relative to the context's module
        parts = context.split(".")
        if len(parts) >= 2:
            module_parts = parts[:-1]
            resolved = ".".join(module_parts) + "." + name
            if resolved in self.symbols:
                return resolved

        # Return as-is if not found
        return name

    def _resolve_call(self, call_name: str, source_symbol: Symbol) -> str:
        """Resolve a function/method call to its qualified name."""
        # If it's already qualified, return as-is
        if "." in call_name:
            return call_name

        # Try same module first
        source_parts = source_symbol.qualified_name.split(".")
        module_parts = source_parts[:-1]

        # If it's a method call on self/cls, try the containing class
        if source_symbol.kind == SymbolKind.METHOD:
            class_name = source_parts[-2] if len(source_parts) >= 2 else None
            if class_name:
                method_qualified = f"{class_name}.{call_name}"
                if method_qualified in self.symbols:
                    return method_qualified

        # Try same module
        same_module = ".".join(module_parts) + "." + call_name
        if same_module in self.symbols:
            return same_module

        # Return as-is if not found
        return call_name

    def get_callers(self, qualified_name: str) -> list[str]:
        """Get all symbols that call the given symbol."""
        if qualified_name not in self.graph:
            return []
        return list(self.graph.predecessors(qualified_name))

    def get_callees(self, qualified_name: str) -> list[str]:
        """Get all symbols called by the given symbol."""
        if qualified_name not in self.graph:
            return []
        return [
            target
            for _, target in self.graph.out_edges(qualified_name)
            if self.graph[qualified_name][target].get("type") == "CALLS"
        ]

    def get_related_symbols(
        self, qualified_name: str, distance: int = 1
    ) -> set[str]:
        """Get related symbols within a given graph distance."""
        related = set()
        if qualified_name not in self.graph:
            return related
        # Get predecessors and successors
        for node in nx.descendants(self.graph, qualified_name):
            d = self._distance_to(qualified_name, node)
            if d is not None and d <= distance:
                related.add(node)
        for node in nx.ancestors(self.graph, qualified_name):
            d = self._distance_to(node, qualified_name)
            if d is not None and d <= distance:
                related.add(node)
        return related

    def _distance_to(self, source: str, target: str) -> Optional[int]:
        """Get the shortest path distance between two nodes."""
        try:
            return nx.shortest_path_length(self.graph, source, target)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None

    def export_symbols(self) -> dict[str, Symbol]:
        """Export all resolved symbols."""
        return self.symbols.copy()
