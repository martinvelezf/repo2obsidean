---
name: SymbolGraph.export_symbols
kind: method
language: python
file: repo2obsidean/graph/builder.py
line: 214
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.export_symbols
  - export_symbols
---

# export_symbols

Export all resolved symbols.

## Signature

```python
def export_symbols(self) -> dict[str, Symbol]
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def export_symbols(self) -> dict[str, Symbol]:
        """Export all resolved symbols."""
        return self.symbols.copy()
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[copy]]



## Related

- [[SymbolGraph]]
- [[copy]]

