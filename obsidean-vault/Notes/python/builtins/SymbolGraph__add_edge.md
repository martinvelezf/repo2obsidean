---
name: SymbolGraph.add_edge
kind: method
language: python
file: /home/martin/lab/obsidean/app/graph/builder.py
line: 29
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.add_edge
  - add_edge
---

# add_edge

Add an edge between two symbols.

## Signature

```python
def add_edge(self, source
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def add_edge(self, source: str, target: str, edge_type: str):
        """Add an edge between two symbols."""
        self.graph.add_edge(source, target, type=edge_type)
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[SymbolGraph__add_edge]]


## Called by

- [[SymbolGraph__add_edge]]
- [[SymbolGraph__build_from_symbols]]


## Related

- [[SymbolGraph]]
- [[SymbolGraph__build_from_symbols]]

