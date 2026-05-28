---
name: slug_from_symbol
kind: function
language: python
file: /home/martin/lab/obsidean/app/generator/slug.py
line: 9
tags: [code, python, function]
aliases:
  - slug_from_symbol
  - slug_from_symbol
---

# slug_from_symbol

Generate a slug (relative path) for a symbol.

## Signature

```python
def slug_from_symbol(symbol
```

## Source

<details>
<summary>Show implementation</summary>

```python
def slug_from_symbol(symbol: Symbol) -> Path:
    """Generate a slug (relative path) for a symbol."""
    parts = symbol.qualified_name.split(".")
    language = symbol.language.value

    if symbol.kind == SymbolKind.CLASS:
        # Class: Notes/python/pkg/module/ClassName.md
        *module_parts, class_name = parts
        module_path = "/".join(module_parts) if module_parts else "builtins"
        filename = f"{class_name}.md"
    elif symbol.kind == SymbolKind.METHOD:
        # Method: Notes/python/pkg/module/ClassName__method_name.md
        # Strip both the method name and the (trailing) class name from the
        # module path so a method sits in the same folder as its class.
        *module_parts, item = parts
        class_name = symbol.parents[0] if symbol.parents else (
     
```

</details>


## Calls

- [[Path]]
- [[join]]
- [[len]]
- [[sanitize_filename]]
- [[sanitize_path]]
- [[split]]


## Called by

- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]


## Related

- [[Path]]
- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[join]]
- [[len]]
- [[sanitize_filename]]
- [[sanitize_path]]
- [[split]]

