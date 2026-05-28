---
name: sanitize_path
kind: function
language: python
file: app/generator/slug.py
line: 46
tags: [code, python, function]
aliases:
  - sanitize_path
  - sanitize_path
---

# sanitize_path

Sanitize a path string for use in filenames.

## Signature

```python
def sanitize_path(path
```

## Source

<details>
<summary>Show implementation</summary>

```python
def sanitize_path(path: str) -> str:
    """Sanitize a path string for use in filenames."""
    # Replace invalid path characters
    path = re.sub(r'[<>:"|?*]', "_", path)
    path = re.sub(r"\s+", "_", path)
    return path
```

</details>


## Calls

- [[sub]]


## Called by

- [[slug_from_symbol]]


## Related

- [[slug_from_symbol]]
- [[sub]]

