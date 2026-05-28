---
name: SymbolGraph._build_odoo_index
kind: method
language: python
file: app/graph/builder.py
line: 75
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph._build_odoo_index
  - _build_odoo_index
---

# _build_odoo_index

Index Odoo models by name and link definitions to extensions.

        This is framework-specific (Odoo) but harmless for any other codebase:
        if no class declares `_name`/`_inherit`, the index is simply empty.

        A class is a *base* of model M when it sets `_name = M` (optionally with
        `_inherit = M`). A class is an *extension* of M when it sets
        `_inherit = M` (or lists M) without redefining `_name`. Mixins pulled in
        via `_inherit`/`_inherits` are also record

## Signature

```python
def _build_odoo_index(self, symbols
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _build_odoo_index(self, symbols: list[Symbol]):
        """Index Odoo models by name and link definitions to extensions.

        This is framework-specific (Odoo) but harmless for any other codebase:
        if no class declares `_name`/`_inherit`, the index is simply empty.

        A class is a *base* of model M when it sets `_name = M` (optionally with
        `_inherit = M`). A class is an *extension* of M when it sets
        `_inherit = M` (or lists M) without redefining `_name`. Mixins pulled in
        via `_inherit`/`_inherits` are also recorded as references to M.
        """
        models: dict[str, dict] = {}

        def slot(model: str) -> dict:
            return models.setdefault(model, {"bases": [], "extensions": [], "refs": []})

        for s in symbols:
      
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[SymbolGraph__add_edge]]
- [[append]]
- [[items]]
- [[setdefault]]
- [[slot]]


## Called by

- [[SymbolGraph__build_from_symbols]]


## Related

- [[SymbolGraph]]
- [[SymbolGraph__add_edge]]
- [[SymbolGraph__build_from_symbols]]
- [[append]]
- [[items]]
- [[setdefault]]
- [[slot]]

