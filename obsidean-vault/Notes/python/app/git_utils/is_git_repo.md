---
name: is_git_repo
kind: function
language: python
file: app/git_utils.py
line: 45
tags: [code, python, function, changed]
changed: true
change_status: M
aliases:
  - is_git_repo
  - is_git_repo
---

# is_git_repo

True if ``root`` is inside a git working tree.

#changed

> [!warning] Changed since git HEAD — status `M`

```diff
@@ -45,0 +46 @@ def is_git_repo(root: Path) -> bool:
+    # demo edit (revert with: git checkout -- app/git_utils.py)
```

## Signature

```python
def is_git_repo(root
```

## Source

<details>
<summary>Show implementation</summary>

```python
def is_git_repo(root: Path) -> bool:
    # demo edit (revert with: git checkout -- app/git_utils.py)
    """True if ``root`` is inside a git working tree."""
    r = _git(root, "rev-parse", "--is-inside-work-tree")
    return r.returncode == 0 and r.stdout.strip() == "true"
```

</details>


## Calls

- [[_git]]
- [[strip]]


## Called by

- [[get_working_tree_changes]]


## Related

- [[_git]]
- [[get_working_tree_changes]]
- [[strip]]

