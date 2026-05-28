---
name: _iter_source_files
kind: function
language: python
file: repo2obsidean/cli.py
line: 45
tags: [code, python, function]
aliases:
  - _iter_source_files
  - _iter_source_files
---

# _iter_source_files

Yield source files for a language, applying ignore/include/exclude rules.

## Signature

```python
def _iter_source_files( repo_path
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _iter_source_files(
    repo_path: Path,
    language: Language,
    include: tuple[str, ...] = (),
    exclude: tuple[str, ...] = (),
):
    """Yield source files for a language, applying ignore/include/exclude rules."""
    seen = set()
    for pattern in LANGUAGE_GLOBS[language]:
        for path in repo_path.glob(pattern):
            if path in seen or any(part in IGNORE_DIRS for part in path.parts):
                continue
            rel = path.relative_to(repo_path).as_posix()
            if include and not _matches_any(rel, path.name, include):
                continue
            if exclude and _matches_any(rel, path.name, exclude):
                continue
            seen.add(path)
            yield path
```

</details>


## Calls

- [[_matches_any]]
- [[add]]
- [[any]]
- [[as_posix]]
- [[glob]]
- [[relative_to]]
- [[set]]


## Called by

- [[_build_vault]]
- [[_detect_languages]]


## Related

- [[_build_vault]]
- [[_detect_languages]]
- [[_matches_any]]
- [[add]]
- [[any]]
- [[as_posix]]
- [[glob]]
- [[relative_to]]
- [[set]]

