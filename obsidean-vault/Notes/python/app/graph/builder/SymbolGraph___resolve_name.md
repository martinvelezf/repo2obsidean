---
name: SymbolGraph._resolve_name
kind: method
language: python
file: app/graph/builder.py
line: 130
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph._resolve_name
  - _resolve_name
---

# _resolve_name

Resolve a name in the given context.

## Signature

```python
def _resolve_name(self, name
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _resolve_name(self, name: str, context: str) -> str:
        """Resolve a name in the given context."""
        # If it's already qualified, return as-is
        if "." in name:
            return name

        # Try to resolve relative to the context's module
        parts = context.split(".")
        if len(parts) >= 2:
            module_parts = parts[:-1]
            resolved = ".".join(module_parts) + "." + name
            if resolved in self.symbols:
                return resolved

        # Return as-is if not found
        return name
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[join]]
- [[len]]
- [[split]]


## Called by

- [[SymbolGraph__build_from_symbols]]


## Related

- [[SymbolGraph]]
- [[SymbolGraph__build_from_symbols]]
- [[join]]
- [[len]]
- [[split]]

