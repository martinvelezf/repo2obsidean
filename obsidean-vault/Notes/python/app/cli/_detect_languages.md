---
name: _detect_languages
kind: function
language: python
file: app/cli.py
line: 66
tags: [code, python, function]
aliases:
  - _detect_languages
  - _detect_languages
---

# _detect_languages

Detect which supported languages are present in the repo.

## Signature

```python
def _detect_languages( repo_path
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _detect_languages(
    repo_path: Path, include: tuple[str, ...] = (), exclude: tuple[str, ...] = ()
) -> list[Language]:
    """Detect which supported languages are present in the repo."""
    found = []
    for lang in LANGUAGE_GLOBS:
        if next(_iter_source_files(repo_path, lang, include, exclude), None) is not None:
            found.append(lang)
    return found
```

</details>


## Calls

- [[_iter_source_files]]
- [[append]]
- [[next]]


## Called by

- [[main]]


## Related

- [[_iter_source_files]]
- [[append]]
- [[main]]
- [[next]]

