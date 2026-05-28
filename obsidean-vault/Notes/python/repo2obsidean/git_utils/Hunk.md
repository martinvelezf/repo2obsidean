---
name: Hunk
kind: class
language: python
file: repo2obsidean/git_utils.py
line: 14
tags: [code, python, class]
aliases:
  - Hunk
  - Hunk
---

# Hunk

A unified-diff hunk, located by its line range in the new file.

## Signature

```python
class Hunk
```

## Source

<details>
<summary>Show full definition</summary>

```python
class Hunk:
    """A unified-diff hunk, located by its line range in the new file."""

    new_start: int
    new_end: int
    text: str
```

</details>

## Decorators

- `@dataclass`



## Called by

- [[_parse_unified_diff]]


## Related

- [[_parse_unified_diff]]

