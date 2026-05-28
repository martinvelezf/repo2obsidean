---
name: _parse_unified_diff
kind: function
language: python
file: repo2obsidean/git_utils.py
line: 97
tags: [code, python, function]
aliases:
  - _parse_unified_diff
  - _parse_unified_diff
---

# _parse_unified_diff

Parse `git diff` output into {file_path: [Hunk, ...]}.

## Signature

```python
def _parse_unified_diff(diff_text
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _parse_unified_diff(diff_text: str, repo_top: Path) -> dict[Path, list[Hunk]]:
    """Parse `git diff` output into {file_path: [Hunk, ...]}."""
    files: dict[Path, list[Hunk]] = {}
    current_file: Path | None = None
    current_hunk: Hunk | None = None
    hunk_lines: list[str] = []

    def flush_hunk():
        nonlocal current_hunk, hunk_lines
        if current_file is not None and current_hunk is not None:
            current_hunk.text = "\n".join(hunk_lines)[:1200]
            files.setdefault(current_file, []).append(current_hunk)
        current_hunk = None
        hunk_lines = []

    for line in diff_text.splitlines():
        if line.startswith("diff --git"):
            # New file section — close any open hunk, reset file until +++.
            flush_hunk()
            
```

</details>


## Calls

- [[Hunk]]
- [[append]]
- [[flush_hunk]]
- [[group]]
- [[int]]
- [[join]]
- [[len]]
- [[match]]
- [[max]]
- [[resolve]]
- [[setdefault]]
- [[splitlines]]
- [[startswith]]
- [[strip]]


## Called by

- [[get_working_tree_changes]]


## Related

- [[Hunk]]
- [[append]]
- [[flush_hunk]]
- [[get_working_tree_changes]]
- [[group]]
- [[int]]
- [[join]]
- [[len]]
- [[match]]
- [[max]]
- [[resolve]]
- [[setdefault]]
- [[splitlines]]
- [[startswith]]
- [[strip]]

