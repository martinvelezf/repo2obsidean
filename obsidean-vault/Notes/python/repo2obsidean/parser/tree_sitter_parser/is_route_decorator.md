---
name: is_route_decorator
kind: function
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 32
tags: [code, python, function]
aliases:
  - is_route_decorator
  - is_route_decorator
---

# is_route_decorator

Heuristic: does any decorator register an HTTP route/endpoint?

    Matches Flask (`@app.route`, `@bp.route`), FastAPI (`@app.get`,
    `@router.post`, `@app.websocket`), and Odoo (`@http.route`, `@route`).
    Bare HTTP verbs (`@get`) are intentionally ignored to avoid false positives;
    a verb only counts when it's a method call on an object (`@app.get`).

## Signature

```python
def is_route_decorator(decorators
```

## Source

<details>
<summary>Show implementation</summary>

```python
def is_route_decorator(decorators: list[str]) -> bool:
    """Heuristic: does any decorator register an HTTP route/endpoint?

    Matches Flask (`@app.route`, `@bp.route`), FastAPI (`@app.get`,
    `@router.post`, `@app.websocket`), and Odoo (`@http.route`, `@route`).
    Bare HTTP verbs (`@get`) are intentionally ignored to avoid false positives;
    a verb only counts when it's a method call on an object (`@app.get`).
    """
    for dec in decorators:
        name = dec.split("(", 1)[0].strip()      # callable before its arguments
        last = name.rsplit(".", 1)[-1]
        if last in _ROUTE_NAMES:
            return True
        if "." in name and last in _ROUTE_VERBS:
            return True
    return False
```

</details>


## Calls

- [[rsplit]]
- [[split]]
- [[strip]]


## Called by

- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser___walk_python]]
- [[rsplit]]
- [[split]]
- [[strip]]

