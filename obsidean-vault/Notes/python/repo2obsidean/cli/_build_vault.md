---
name: _build_vault
kind: function
language: python
file: repo2obsidean/cli.py
line: 77
tags: [code, python, function]
aliases:
  - _build_vault
  - _build_vault
---

# _build_vault

Run the full pipeline over one or more (path, layer) roots.

    ``layer`` is "" for a single root (cleaner paths) or the folder name when
    multiple roots are given (e.g. odoo / user / enterprise).

    Returns (symbol_count, changed_symbol_count).

## Signature

```python
def _build_vault( roots
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _build_vault(
    roots: list[tuple[Path, str]],
    out: Path,
    languages: list[Language],
    include: tuple[str, ...] = (),
    exclude: tuple[str, ...] = (),
    use_git: bool = True,
) -> tuple[int, int]:
    """Run the full pipeline over one or more (path, layer) roots.

    ``layer`` is "" for a single root (cleaner paths) or the folder name when
    multiple roots are given (e.g. odoo / user / enterprise).

    Returns (symbol_count, changed_symbol_count).
    """
    graph = SymbolGraph()
    parsers = {lang: TreeSitterParser(lang) for lang in languages}
    all_symbols = []

    for root, layer in roots:
        label = f"[{layer}] " if layer else ""
        for lang in languages:
            files = list(_iter_source_files(root, lang, include, exclude))
            if not
```

</details>


## Calls

- [[SymbolGraph]]
- [[TreeSitterParser]]
- [[VaultGenerator]]
- [[_iter_source_files]]
- [[_stamp_git_changes]]
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
- [[_stamp_git_changes]]
- [[build_from_symbols]]
- [[echo]]
- [[extend]]
- [[generate]]
- [[len]]
- [[list]]
- [[main]]
- [[parse_file]]
- [[progressbar]]

