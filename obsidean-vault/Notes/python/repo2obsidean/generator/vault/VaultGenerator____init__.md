---
name: VaultGenerator.__init__
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 17
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator.__init__
  - __init__
---

# __init__



## Signature

```python
def __init__(self, output_dir
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.notes_dir = self.output_dir / "Notes"
        self.env = self._setup_jinja()
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[Path]]
- [[VaultGenerator___setup_jinja]]



## Related

- [[Path]]
- [[VaultGenerator]]
- [[VaultGenerator___setup_jinja]]

