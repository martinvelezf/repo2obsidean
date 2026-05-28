---
name: ChangeInfo
kind: class
language: python
file: app/git_utils.py
line: 23
tags: [code, python, class]
aliases:
  - ChangeInfo
  - ChangeInfo
---

# ChangeInfo

Working-tree change state for a single file.

## Signature

```python
class ChangeInfo
```

## Source

<details>
<summary>Show full definition</summary>

```python
class ChangeInfo:
    """Working-tree change state for a single file."""

    status: str  # "M" | "A" | "D"
    hunks: list[Hunk] = field(default_factory=list)
```

</details>

## Decorators

- `@dataclass`



## Called by

- [[get_working_tree_changes]]


## Related

- [[get_working_tree_changes]]

