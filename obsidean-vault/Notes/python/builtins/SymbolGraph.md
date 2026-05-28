---
name: SymbolGraph
kind: class
language: python
file: /home/martin/lab/obsidean/app/graph/builder.py
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
        """Build the graph from 
```

</details>



## Called by

- [[SymbolGraph____init__]]
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

