---
name: SymbolGraph.__init__
kind: method
language: python
file: app/graph/builder.py
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
        # Full, un-deduplicated symbol list (identically-named classes across
        # layers all survive here, unlike the qualified_name-keyed dict above).
        self.all_symbols: list[Symbol] = []
        # Odoo model name -> {"bases": [...], "extensions": [...]}
        self.odoo_models: dict[str, dict] = {}
        # Model names referenced via _inherit/_inherits with no base definition.
        self.odoo_unresolved: dict[str, list[Symbol]] = {}
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[DiGraph]]



## Related

- [[DiGraph]]
- [[SymbolGraph]]

