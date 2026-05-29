---
name: VaultGenerator._generate_index
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 269
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._generate_index
  - _generate_index
---

# _generate_index

Generate the index.md file.

## Signature

```python
def _generate_index(self, symbols
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _generate_index(self, symbols: dict[str, Symbol]):
        """Generate the index.md file."""
        index_path = self.notes_dir / "index.md"

        # Group symbols by language
        by_language = {}
        for qname, symbol in symbols.items():
            lang = symbol.language.value
            if lang not in by_language:
                by_language[lang] = []
            by_language[lang].append(symbol)

        content = "# Codebase Index\n\n"
        for lang in sorted(by_language.keys()):
            content += f"## {lang.capitalize()}\n\n"
            # Group by module
            by_module = {}
            for symbol in by_language[lang]:
                parts = symbol.qualified_name.split(".")
                module = ".".join(parts[:-1]) if len(parts) > 1 else "_root
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
- [[relative_to]]
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
- [[relative_to]]
- [[slug_from_symbol]]
- [[sorted]]
- [[split]]
- [[write_text]]

