---
name: _file_tail
kind: function
language: python
file: app/generator/slug.py
line: 39
tags: [code, python, function]
aliases:
  - _file_tail
  - _file_tail
---

# _file_tail

Return the last ``depth`` path components of a file, sans extension.

## Signature

```python
def _file_tail(file_path, depth
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _file_tail(file_path, depth: int = 3) -> list[str]:
    """Return the last ``depth`` path components of a file, sans extension."""
    p = Path(file_path).with_suffix("")
    parts = [part for part in p.parts if part not in ("", "/")]
    return parts[-depth:] if parts else ["module"]
```

</details>


## Calls

- [[Path]]
- [[with_suffix]]


## Called by

- [[slug_from_symbol]]


## Related

- [[Path]]
- [[slug_from_symbol]]
- [[with_suffix]]

