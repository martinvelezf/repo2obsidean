---
name: VaultGenerator._setup_jinja
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 23
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._setup_jinja
  - _setup_jinja
---

# _setup_jinja

Set up Jinja2 environment.

        Autoescape is OFF: we emit Markdown, not HTML, so escaping quotes/angle
        brackets in source snippets would corrupt the output.

## Signature

```python
def _setup_jinja(self) -> Environment
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _setup_jinja(self) -> Environment:
        """Set up Jinja2 environment.

        Autoescape is OFF: we emit Markdown, not HTML, so escaping quotes/angle
        brackets in source snippets would corrupt the output.
        """
        template_dir = Path(__file__).parent / "templates"
        return Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[Environment]]
- [[FileSystemLoader]]
- [[Path]]


## Called by

- [[VaultGenerator____init__]]


## Related

- [[Environment]]
- [[FileSystemLoader]]
- [[Path]]
- [[VaultGenerator]]
- [[VaultGenerator____init__]]

