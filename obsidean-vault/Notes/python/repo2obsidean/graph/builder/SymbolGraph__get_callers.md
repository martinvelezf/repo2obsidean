---
name: SymbolGraph.get_callers
kind: method
language: python
file: repo2obsidean/graph/builder.py
line: 173
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.get_callers
  - get_callers
---

# get_callers

Get all symbols that call the given symbol.

## Signature

```python
def get_callers(self, qualified_name
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def get_callers(self, qualified_name: str) -> list[str]:
        """Get all symbols that call the given symbol."""
        if qualified_name not in self.graph:
            return []
        return list(self.graph.predecessors(qualified_name))
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[list]]
- [[predecessors]]



## Related

- [[SymbolGraph]]
- [[list]]
- [[predecessors]]

