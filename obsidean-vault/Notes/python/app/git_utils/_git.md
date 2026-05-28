---
name: _git
kind: function
language: python
file: app/git_utils.py
line: 33
tags: [code, python, function]
aliases:
  - _git
  - _git
---

# _git

Run a git command in ``root`` and capture output (never raises).

## Signature

```python
def _git(root
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    """Run a git command in ``root`` and capture output (never raises)."""
    try:
        return subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        # git not installed
        return subprocess.CompletedProcess(args, 1, "", "git not found")
```

</details>


## Calls

- [[CompletedProcess]]
- [[run]]
- [[str]]


## Called by

- [[get_working_tree_changes]]
- [[is_git_repo]]


## Related

- [[CompletedProcess]]
- [[get_working_tree_changes]]
- [[is_git_repo]]
- [[run]]
- [[str]]

