---
name: VaultGenerator._unique_path
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 107
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._unique_path
  - _unique_path
---

# _unique_path

Return a non-colliding path, appending -2, -3, ... if needed.

## Signature

```python
def _unique_path(self, path
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _unique_path(self, path: Path) -> Path:
        """Return a non-colliding path, appending -2, -3, ... if needed."""
        if path not in self._written_paths:
            self._written_paths.add(path)
            return path
        stem, suffix = path.stem, path.suffix
        i = 2
        while True:
            candidate = path.with_name(f"{stem}-{i}{suffix}")
            if candidate not in self._written_paths:
                self._written_paths.add(candidate)
                return candidate
            i += 1
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[add]]
- [[with_name]]


## Called by

- [[VaultGenerator___generate_note]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator___generate_note]]
- [[add]]
- [[with_name]]

