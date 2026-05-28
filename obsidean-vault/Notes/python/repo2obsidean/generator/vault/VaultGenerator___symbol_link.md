---
name: VaultGenerator._symbol_link
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 168
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._symbol_link
  - _symbol_link
---

# _symbol_link

Wikilink text matching the symbol's note filename (sans .md).

## Signature

```python
def _symbol_link(self, symbol
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _symbol_link(self, symbol: Symbol) -> str:
        """Wikilink text matching the symbol's note filename (sans .md)."""
        if symbol.kind == SymbolKind.METHOD and symbol.parents:
            return f"{symbol.parents[0]}__{symbol.name}"
        return symbol.name
```

</details>


## Parent

- [[VaultGenerator]]



## Called by

- [[VaultGenerator___generate_recent_changes]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator___generate_recent_changes]]

