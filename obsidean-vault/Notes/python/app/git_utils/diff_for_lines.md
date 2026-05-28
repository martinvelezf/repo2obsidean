---
name: diff_for_lines
kind: function
language: python
file: app/git_utils.py
line: 142
tags: [code, python, function]
aliases:
  - diff_for_lines
  - diff_for_lines
---

# diff_for_lines

Return the diff hunks overlapping a symbol's [start_line, end_line].

## Signature

```python
def diff_for_lines(info
```

## Source

<details>
<summary>Show implementation</summary>

```python
def diff_for_lines(info: ChangeInfo, start_line: int, end_line: int) -> str:
    # demo edit (revert with: git checkout -- app/git_utils.py)
    """Return the diff hunks overlapping a symbol's [start_line, end_line]."""
    if info.status == "A":
        return "(new file — not yet committed)"
    if info.status == "D":
        return "(file deleted)"
    overlapping = [
        h.text for h in info.hunks
        if h.new_start <= end_line and h.new_end >= start_line
    ]
    return "\n".join(overlapping)[:1500]
```

</details>


## Calls

- [[join]]


## Called by

- [[_stamp_git_changes]]


## Related

- [[_stamp_git_changes]]
- [[join]]

