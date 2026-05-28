---
name: get_working_tree_changes
kind: function
language: python
file: app/git_utils.py
line: 52
tags: [code, python, function]
aliases:
  - get_working_tree_changes
  - get_working_tree_changes
---

# get_working_tree_changes

Return {resolved_file_path: ChangeInfo} for uncommitted changes.

    Combines staged + unstaged + untracked, i.e. everything that differs from
    HEAD in the working tree.

## Signature

```python
def get_working_tree_changes(root
```

## Source

<details>
<summary>Show implementation</summary>

```python
def get_working_tree_changes(root: Path) -> dict[Path, ChangeInfo]:
    # demo edit (revert with: git checkout -- app/git_utils.py)
    """Return {resolved_file_path: ChangeInfo} for uncommitted changes.

    Combines staged + unstaged + untracked, i.e. everything that differs from
    HEAD in the working tree.
    """
    if not is_git_repo(root):
        return {}

    top = _git(root, "rev-parse", "--show-toplevel").stdout.strip()
    repo_top = Path(top) if top else Path(root)

    changes: dict[Path, ChangeInfo] = {}

    # 1) Which files changed (incl. untracked) and their coarse status.
    status = _git(root, "status", "--porcelain", "--untracked-files=all").stdout
    for line in status.splitlines():
        if not line.strip():
            continue
        code = line[:2]
       
```

</details>


## Calls

- [[ChangeInfo]]
- [[Path]]
- [[_git]]
- [[_parse_unified_diff]]
- [[is_git_repo]]
- [[items]]
- [[resolve]]
- [[split]]
- [[splitlines]]
- [[strip]]


## Called by

- [[_stamp_git_changes]]


## Related

- [[ChangeInfo]]
- [[Path]]
- [[_git]]
- [[_parse_unified_diff]]
- [[_stamp_git_changes]]
- [[is_git_repo]]
- [[items]]
- [[resolve]]
- [[split]]
- [[splitlines]]
- [[strip]]

