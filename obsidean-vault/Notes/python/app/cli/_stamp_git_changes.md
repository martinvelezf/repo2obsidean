---
name: _stamp_git_changes
kind: function
language: python
file: app/cli.py
line: 119
tags: [code, python, function]
aliases:
  - _stamp_git_changes
  - _stamp_git_changes
---

# _stamp_git_changes

Mark symbols whose source file has uncommitted changes. Returns count.

## Signature

```python
def _stamp_git_changes(roots
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _stamp_git_changes(roots: list[tuple[Path, str]], symbols: list) -> int:
    """Mark symbols whose source file has uncommitted changes. Returns count."""
    all_changes = {}
    for root, _ in roots:
        all_changes.update(get_working_tree_changes(root))
    if not all_changes:
        return 0

    for s in symbols:
        info = all_changes.get(Path(s.file).resolve())
        if info is None:
            continue
        if info.status in ("A", "D"):
            # New or deleted file: every symbol in it is affected.
            s.changed = True
            s.change_status = info.status
            s.change_diff = diff_for_lines(info, s.start_line, s.end_line)
        else:
            # Modified file: flag only symbols whose lines overlap a hunk.
            diff = diff_for_lin
```

</details>


## Calls

- [[Path]]
- [[diff_for_lines]]
- [[get]]
- [[get_working_tree_changes]]
- [[resolve]]
- [[sum]]
- [[update]]


## Called by

- [[_build_vault]]


## Related

- [[Path]]
- [[_build_vault]]
- [[diff_for_lines]]
- [[get]]
- [[get_working_tree_changes]]
- [[resolve]]
- [[sum]]
- [[update]]

