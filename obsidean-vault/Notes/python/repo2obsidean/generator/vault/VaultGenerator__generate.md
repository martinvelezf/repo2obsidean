---
name: VaultGenerator.generate
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 36
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

## Signature

```python
def generate(self, graph
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def generate(self, graph: SymbolGraph):
        """Generate the vault from a symbol graph.

        Only the generated ``Notes/`` content is wiped and rebuilt. Anything
        else in the output directory — notably Obsidian's own ``.obsidian/``
        config (graph color groups, workspace, appearance) — is preserved, so
        regenerating doesn't blow away the user's graph setup.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if self.notes_dir.exists():
            shutil.rmtree(self.notes_dir)
        self.notes_dir.mkdir(parents=True)

        # Iterate the full list (not the deduped dict) so identically-named
        # classes across files/layers each get their own note.
        self._written_paths: set[Path] = set()
        for symbol in graph.al
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
- [[exists]]
- [[export_symbols]]
- [[mkdir]]
- [[rmtree]]
- [[set]]

