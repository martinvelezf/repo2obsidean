---
name: sanitize_filename
kind: function
language: python
file: repo2obsidean/generator/slug.py
line: 54
tags: [code, python, function]
aliases:
  - sanitize_filename
  - sanitize_filename
---

# sanitize_filename

Sanitize a filename.

## Signature

```python
def sanitize_filename(filename
```

## Source

<details>
<summary>Show implementation</summary>

```python
def sanitize_filename(filename: str) -> str:
    """Sanitize a filename."""
    # Remove invalid characters
    filename = re.sub(r'[<>:"|?*]', "_", filename)
    filename = re.sub(r"\s+", "_", filename)
    # Remove leading/trailing dots and spaces
    filename = filename.strip(". ")
    return filename
```

</details>


## Calls

- [[strip]]
- [[sub]]


## Called by

- [[slug_from_symbol]]


## Related

- [[slug_from_symbol]]
- [[strip]]
- [[sub]]

