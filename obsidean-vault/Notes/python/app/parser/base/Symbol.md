---
name: Symbol
kind: class
language: python
file: app/parser/base.py
line: 23
tags: [code, python, class]
aliases:
  - Symbol
  - Symbol
---

# Symbol

Represents a code symbol (class, method, function, etc.).

## Signature

```python
class Symbol
```

## Source

<details>
<summary>Show full definition</summary>

```python
class Symbol:
    """Represents a code symbol (class, method, function, etc.)."""

    name: str
    kind: SymbolKind
    language: Language
    qualified_name: str
    file: Path
    start_line: int
    end_line: int
    signature: str
    docstring: str = ""
    source_snippet: str = ""
    calls: list[str] = field(default_factory=list)
    parents: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)

    # Source root this symbol came from (e.g. "odoo", "user", "enterprise").
    # Used to disambiguate identically-named classes across addon trees.
    layer: str = ""

    # Odoo ORM model metadata (None/empty for non-Odoo code).
    # odoo_model     -> value of `_name`
    # odoo_inherit   -
```

</details>

## Decorators

- `@dataclass`



## Called by

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_js]]
- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_js]]
- [[TreeSitterParser___walk_python]]

