---
name: _iter_source_files
kind: function
language: python
file: /home/martin/lab/obsidean/app/cli.py
line: 27
tags: [code, python, function]
aliases:
  - _iter_source_files
  - _iter_source_files
---

# _iter_source_files

Yield source files for a language, skipping ignored directories.

## Signature

```python
def _iter_source_files(repo_path
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _iter_source_files(repo_path: Path, language: Language):
    """Yield source files for a language, skipping ignored directories."""
    for path in repo_path.glob(LANGUAGE_GLOBS[language]):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        yield path
```

</details>


## Calls

- [[any]]
- [[glob]]


## Called by

- [[_build_vault]]
- [[_detect_languages]]


## Related

- [[_build_vault]]
- [[_detect_languages]]
- [[any]]
- [[glob]]

