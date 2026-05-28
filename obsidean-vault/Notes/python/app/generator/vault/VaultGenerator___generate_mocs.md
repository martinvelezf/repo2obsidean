---
name: VaultGenerator._generate_mocs
kind: method
language: python
file: app/generator/vault.py
line: 261
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._generate_mocs
  - _generate_mocs
---

# _generate_mocs

Generate Maps of Content for each language and module.

## Signature

```python
def _generate_mocs(self, symbols
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _generate_mocs(self, symbols: dict[str, Symbol], graph: SymbolGraph):
        """Generate Maps of Content for each language and module."""
        # Group by language
        by_language = {}
        for qname, symbol in symbols.items():
            lang = symbol.language.value
            if lang not in by_language:
                by_language[lang] = []
            by_language[lang].append(symbol)

        # Generate language-level MOC
        for lang in by_language.keys():
            moc_path = self.notes_dir / f"MOC-{lang}.md"
            content = f"# {lang.capitalize()} Symbols\n\n"

            by_module = {}
            for symbol in by_language[lang]:
                parts = symbol.qualified_name.split(".")
                module = ".".join(parts[:-1]) if len(parts) > 1 
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[append]]
- [[capitalize]]
- [[items]]
- [[join]]
- [[keys]]
- [[len]]
- [[slug_from_symbol]]
- [[sorted]]
- [[split]]
- [[write_text]]


## Called by

- [[VaultGenerator__generate]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator__generate]]
- [[append]]
- [[capitalize]]
- [[items]]
- [[join]]
- [[keys]]
- [[len]]
- [[slug_from_symbol]]
- [[sorted]]
- [[split]]
- [[write_text]]

