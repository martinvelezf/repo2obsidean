---
name: SymbolGraph
kind: class
language: python
file: repo2obsidean/graph/builder.py
line: 11
tags: [code, python, class]
aliases:
  - SymbolGraph
  - SymbolGraph
---

# SymbolGraph

A directed graph of code symbols and their relationships.

## Signature

```python
class SymbolGraph
```

## Source

<details>
<summary>Show full definition</summary>

```python
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
        self.gra
```

</details>



## Called by

- [[SymbolGraph____init__]]
- [[SymbolGraph___build_odoo_index]]
- [[SymbolGraph___distance_to]]
- [[SymbolGraph___resolve_call]]
- [[SymbolGraph___resolve_name]]
- [[SymbolGraph__add_edge]]
- [[SymbolGraph__add_symbol]]
- [[SymbolGraph__build_from_symbols]]
- [[SymbolGraph__export_symbols]]
- [[SymbolGraph__get_callees]]
- [[SymbolGraph__get_callers]]
- [[SymbolGraph__get_related_symbols]]
- [[_build_vault]]


## Related

- [[SymbolGraph____init__]]
- [[SymbolGraph___build_odoo_index]]
- [[SymbolGraph___distance_to]]
- [[SymbolGraph___resolve_call]]
- [[SymbolGraph___resolve_name]]
- [[SymbolGraph__add_edge]]
- [[SymbolGraph__add_symbol]]
- [[SymbolGraph__build_from_symbols]]
- [[SymbolGraph__export_symbols]]
- [[SymbolGraph__get_callees]]
- [[SymbolGraph__get_callers]]
- [[SymbolGraph__get_related_symbols]]
- [[_build_vault]]

