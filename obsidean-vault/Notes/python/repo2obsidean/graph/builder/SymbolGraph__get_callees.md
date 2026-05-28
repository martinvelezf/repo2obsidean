---
name: SymbolGraph.get_callees
kind: method
language: python
file: repo2obsidean/graph/builder.py
line: 179
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.get_callees
  - get_callees
---

# get_callees

Get all symbols called by the given symbol.

## Signature

```python
def get_callees(self, qualified_name
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def get_callees(self, qualified_name: str) -> list[str]:
        """Get all symbols called by the given symbol."""
        if qualified_name not in self.graph:
            return []
        return [
            target
            for _, target in self.graph.out_edges(qualified_name)
            if self.graph[qualified_name][target].get("type") == "CALLS"
        ]
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[get]]
- [[out_edges]]



## Related

- [[SymbolGraph]]
- [[get]]
- [[out_edges]]

