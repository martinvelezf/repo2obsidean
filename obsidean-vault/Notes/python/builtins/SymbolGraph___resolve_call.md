---
name: SymbolGraph._resolve_call
kind: method
language: python
file: /home/martin/lab/obsidean/app/graph/builder.py
line: 80
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph._resolve_call
  - _resolve_call
---

# _resolve_call

Resolve a function/method call to its qualified name.

## Signature

```python
def _resolve_call(self, call_name
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _resolve_call(self, call_name: str, source_symbol: Symbol) -> str:
        """Resolve a function/method call to its qualified name."""
        # If it's already qualified, return as-is
        if "." in call_name:
            return call_name

        # Try same module first
        source_parts = source_symbol.qualified_name.split(".")
        module_parts = source_parts[:-1]

        # If it's a method call on self/cls, try the containing class
        if source_symbol.kind == SymbolKind.METHOD:
            class_name = source_parts[-2] if len(source_parts) >= 2 else None
            if class_name:
                method_qualified = f"{class_name}.{call_name}"
                if method_qualified in self.symbols:
                    return method_qualified

        # Try same modu
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

