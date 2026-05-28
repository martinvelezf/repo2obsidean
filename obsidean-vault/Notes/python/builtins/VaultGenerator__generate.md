---
name: VaultGenerator.generate
kind: method
language: python
file: /home/martin/lab/obsidean/app/generator/vault.py
line: 36
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator.generate
  - generate
---

# generate

Generate the vault from a symbol graph.

## Signature

```python
def generate(self, graph
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def generate(self, graph: SymbolGraph):
        """Generate the vault from a symbol graph."""
        # Clean output directory
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)
        self.notes_dir.mkdir(parents=True)

        symbols = graph.export_symbols()

        # Generate note for each symbol
        for qualified_name, symbol in symbols.items():
            if not qualified_name.startswith("?"):  # Skip unresolved
                self._generate_note(symbol, graph)

        # Generate index
        self._generate_index(symbols)

        # Generate MOCs (maps of content)
        self._generate_mocs(symbols, graph)
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[exists]]
- [[export_symbols]]
- [[items]]
- [[mkdir]]
- [[rmtree]]
- [[startswith]]



## Related

- [[VaultGenerator]]
- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[exists]]
- [[export_symbols]]
- [[items]]
- [[mkdir]]
- [[rmtree]]
- [[startswith]]

