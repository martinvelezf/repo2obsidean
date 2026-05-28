---
name: SymbolGraph._distance_to
kind: method
language: python
file: /home/martin/lab/obsidean/app/graph/builder.py
line: 140
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph._distance_to
  - _distance_to
---

# _distance_to

Get the shortest path distance between two nodes.

## Signature

```python
def _distance_to(self, source
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _distance_to(self, source: str, target: str) -> Optional[int]:
        """Get the shortest path distance between two nodes."""
        try:
            return nx.shortest_path_length(self.graph, source, target)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[shortest_path_length]]


## Called by

- [[SymbolGraph__get_related_symbols]]


## Related

- [[SymbolGraph]]
- [[SymbolGraph__get_related_symbols]]
- [[shortest_path_length]]

