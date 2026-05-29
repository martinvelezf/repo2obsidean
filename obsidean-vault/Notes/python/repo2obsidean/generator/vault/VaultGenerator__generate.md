---
name: VaultGenerator.generate
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 37
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator.generate
  - generate
---

# generate

Generate the vault from a symbol graph.

        Only the generated ``Notes/`` content is wiped and rebuilt. Anything
        else in the output directory — notably Obsidian's own ``.obsidian/``
        config (graph color groups, workspace, appearance) — is preserved, so
        regenerating doesn't blow away the user's graph setup.

        Set ``reset_graph_config=True`` to re-seed the default colour groups
        (changed/route/class/method/function) even when graph.json exists.
        Oth

## Signature

```python
def generate(self, graph
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def generate(self, graph: SymbolGraph, *, reset_graph_config: bool = False):
        """Generate the vault from a symbol graph.

        Only the generated ``Notes/`` content is wiped and rebuilt. Anything
        else in the output directory — notably Obsidian's own ``.obsidian/``
        config (graph color groups, workspace, appearance) — is preserved, so
        regenerating doesn't blow away the user's graph setup.

        Set ``reset_graph_config=True`` to re-seed the default colour groups
        (changed/route/class/method/function) even when graph.json exists.
        Other settings (scale, display, forces) are merged-preserved.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if self.notes_dir.exists():
            shutil.rmtree(self.notes_dir)

```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[VaultGenerator___generate_odoo_report]]
- [[VaultGenerator___generate_recent_changes]]
- [[VaultGenerator___seed_graph_config]]
- [[exists]]
- [[export_symbols]]
- [[mkdir]]
- [[rmtree]]
- [[set]]



## Related

- [[VaultGenerator]]
- [[VaultGenerator___generate_index]]
- [[VaultGenerator___generate_mocs]]
- [[VaultGenerator___generate_note]]
- [[VaultGenerator___generate_odoo_report]]
- [[VaultGenerator___generate_recent_changes]]
- [[VaultGenerator___seed_graph_config]]
- [[exists]]
- [[export_symbols]]
- [[mkdir]]
- [[rmtree]]
- [[set]]

