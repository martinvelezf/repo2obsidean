---
name: _matches_any
kind: function
language: python
file: app/cli.py
line: 31
tags: [code, python, function]
aliases:
  - _matches_any
  - _matches_any
---

# _matches_any

True if the path matches any glob.

    Matches against the full root-relative path, the bare filename, AND every
    trailing sub-path, so a pattern like ``models/**`` targets a directory at
    any depth (e.g. ``sale/models/foo.py``), not just at the root.

## Signature

```python
def _matches_any(rel_path
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _matches_any(rel_path: str, name: str, patterns: tuple[str, ...]) -> bool:
    """True if the path matches any glob.

    Matches against the full root-relative path, the bare filename, AND every
    trailing sub-path, so a pattern like ``models/**`` targets a directory at
    any depth (e.g. ``sale/models/foo.py``), not just at the root.
    """
    parts = rel_path.split("/")
    _fake_test()
    candidates = {rel_path, name}
    candidates.update("/".join(parts[i:]) for i in range(len(parts)))
    return any(fnmatch.fnmatch(c, p) for c in candidates for p in patterns)
```

</details>


## Calls

- [[_fake_test]]
- [[any]]
- [[fnmatch]]
- [[join]]
- [[len]]
- [[range]]
- [[split]]
- [[update]]


## Called by

- [[_iter_source_files]]


## Related

- [[_fake_test]]
- [[_iter_source_files]]
- [[any]]
- [[fnmatch]]
- [[join]]
- [[len]]
- [[range]]
- [[split]]
- [[update]]

