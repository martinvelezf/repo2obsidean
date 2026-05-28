---
name: SymbolGraph.__init__
kind: method
language: python
file: /home/martin/lab/obsidean/app/graph/builder.py
line: 14
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.__init__
  - __init__
---

# __init__



## Signature

```python
def __init__(self)
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def __init__(self):
        self.graph = nx.DiGraph()
        self.symbols: dict[str, Symbol] = {}
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[DiGraph]]



## Related

- [[DiGraph]]
- [[SymbolGraph]]

