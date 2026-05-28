---
name: SymbolGraph.get_related_symbols
kind: method
language: python
file: /home/martin/lab/obsidean/app/graph/builder.py
line: 122
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.get_related_symbols
  - get_related_symbols
---

# get_related_symbols

Get related symbols within a given graph distance.

## Signature

```python
def get_related_symbols( self, qualified_name
```

## Source

<details>
<summary>Show implementation</summary>

```python
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
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[SymbolGraph___distance_to]]
- [[add]]
- [[ancestors]]
- [[descendants]]
- [[set]]



## Related

- [[SymbolGraph]]
- [[SymbolGraph___distance_to]]
- [[add]]
- [[ancestors]]
- [[descendants]]
- [[set]]

