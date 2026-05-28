---
name: SymbolGraph.add_symbol
kind: method
language: python
file: app/graph/builder.py
line: 25
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.add_symbol
  - add_symbol
---

# add_symbol

Add a symbol to the graph.

## Signature

```python
def add_symbol(self, symbol
```

## Source

<details>
<summary>Show implementation</summary>

```python
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
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[add_node]]


## Called by

- [[SymbolGraph__build_from_symbols]]


## Related

- [[SymbolGraph]]
- [[SymbolGraph__build_from_symbols]]
- [[add_node]]

