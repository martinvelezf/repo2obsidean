---
name: _build_vault
kind: function
language: python
file: /home/martin/lab/obsidean/app/cli.py
line: 44
tags: [code, python, function]
aliases:
  - _build_vault
  - _build_vault
---

# _build_vault

Run the full pipeline. Returns the number of symbols extracted.

## Signature

```python
def _build_vault(repo_path
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _build_vault(repo_path: Path, out: Path, languages: list[Language]) -> int:
    """Run the full pipeline. Returns the number of symbols extracted."""
    graph = SymbolGraph()
    all_symbols = []

    for lang in languages:
        parser = TreeSitterParser(lang)
        files = list(_iter_source_files(repo_path, lang))
        click.echo(f"  {lang.value}: {len(files)} files")
        with click.progressbar(files, label=f"  parsing {lang.value}") as bar:
            for file_path in bar:
                try:
                    all_symbols.extend(parser.parse_file(file_path))
                except Exception as e:  # noqa: BLE001
                    click.echo(f"\n  ! error parsing {file_path}: {e}", err=True)

    graph.build_from_symbols(all_symbols)
    VaultGenerator(out).generate
```

</details>


## Calls

- [[SymbolGraph]]
- [[TreeSitterParser]]
- [[VaultGenerator]]
- [[_iter_source_files]]
- [[build_from_symbols]]
- [[echo]]
- [[extend]]
- [[generate]]
- [[len]]
- [[list]]
- [[parse_file]]
- [[progressbar]]


## Called by

- [[main]]


## Related

- [[SymbolGraph]]
- [[TreeSitterParser]]
- [[VaultGenerator]]
- [[_iter_source_files]]
- [[build_from_symbols]]
- [[echo]]
- [[extend]]
- [[generate]]
- [[len]]
- [[list]]
- [[main]]
- [[parse_file]]
- [[progressbar]]

