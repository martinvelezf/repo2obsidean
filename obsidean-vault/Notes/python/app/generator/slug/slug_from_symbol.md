---
name: slug_from_symbol
kind: function
language: python
file: app/generator/slug.py
line: 9
tags: [code, python, function]
aliases:
  - slug_from_symbol
  - slug_from_symbol
---

# slug_from_symbol

Generate a slug (relative path) for a symbol.

    Layout: ``Notes/<language>/<layer?>/<source-file-path>/<filename>.md``

    Notes are grouped by their source file (last few path components) so that
    identically-named classes living in different modules/addons don't collide,
    and a layer label (odoo/user/enterprise) keeps the trees separate.

## Signature

```python
def slug_from_symbol(symbol
```

## Source

<details>
<summary>Show implementation</summary>

```python
def slug_from_symbol(symbol: Symbol) -> Path:
    """Generate a slug (relative path) for a symbol.

    Layout: ``Notes/<language>/<layer?>/<source-file-path>/<filename>.md``

    Notes are grouped by their source file (last few path components) so that
    identically-named classes living in different modules/addons don't collide,
    and a layer label (odoo/user/enterprise) keeps the trees separate.
    """
    language = symbol.language.value

    # Filename derives from the symbol kind and name.
    if symbol.kind == SymbolKind.METHOD:
        class_name = symbol.parents[0] if symbol.parents else ""
        filename = f"{class_name}__{symbol.name}.md" if class_name else f"{symbol.name}.md"
    else:
        filename = f"{symbol.name}.md"

    # Folder derives from layer + the source fi
```

</details>


## Calls

- [[Path]]
- [[_file_tail]]
- [[append]]
- [[extend]]
- [[join]]
- [[sanitize_filename]]
- [[sanitize_path]]


## Called by

- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]


## Related

- [[Path]]
- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[_file_tail]]
- [[append]]
- [[extend]]
- [[join]]
- [[sanitize_filename]]
- [[sanitize_path]]

