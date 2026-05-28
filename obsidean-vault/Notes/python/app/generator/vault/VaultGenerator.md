---
name: VaultGenerator
kind: class
language: python
file: app/generator/vault.py
line: 14
tags: [code, python, class]
aliases:
  - VaultGenerator
  - VaultGenerator
---

# VaultGenerator

Generate an Obsidian vault from a symbol graph.

## Signature

```python
class VaultGenerator
```

## Source

<details>
<summary>Show full definition</summary>

```python
class VaultGenerator:
    """Generate an Obsidian vault from a symbol graph."""

    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.notes_dir = self.output_dir / "Notes"
        self.env = self._setup_jinja()

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

    def generate(self, graph: SymbolGraph):
        """Generate th
```

</details>



## Called by

- [[VaultGenerator____init__]]
- [[VaultGenerator___format_links]]
- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[VaultGenerator___generate_odoo_report]]
- [[VaultGenerator___generate_recent_changes]]
- [[VaultGenerator___setup_jinja]]
- [[VaultGenerator___symbol_link]]
- [[VaultGenerator___unique_path]]
- [[VaultGenerator__generate]]
- [[_build_vault]]


## Related

- [[VaultGenerator____init__]]
- [[VaultGenerator___format_links]]
- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[VaultGenerator___generate_odoo_report]]
- [[VaultGenerator___generate_recent_changes]]
- [[VaultGenerator___setup_jinja]]
- [[VaultGenerator___symbol_link]]
- [[VaultGenerator___unique_path]]
- [[VaultGenerator__generate]]
- [[_build_vault]]

