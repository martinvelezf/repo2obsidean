---
name: VaultGenerator._seed_graph_config
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 86
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._seed_graph_config
  - _seed_graph_config
---

# _seed_graph_config

Seed default colour groups; preserve everything else.

        - File absent → write a fresh ``graph.json`` with the defaults.
        - File present, ``reset=False`` → leave it alone (don't trash customised groups).
        - File present, ``reset=True`` → replace only ``colorGroups``; keep other
          settings (display/forces/scale) so Obsidian doesn't reset your view.

## Signature

```python
def _seed_graph_config(self, reset
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _seed_graph_config(self, reset: bool = False):
        """Seed default colour groups; preserve everything else.

        - File absent → write a fresh ``graph.json`` with the defaults.
        - File present, ``reset=False`` → leave it alone (don't trash customised groups).
        - File present, ``reset=True`` → replace only ``colorGroups``; keep other
          settings (display/forces/scale) so Obsidian doesn't reset your view.
        """
        graph_json = self.output_dir / ".obsidian" / "graph.json"
        if graph_json.exists() and not reset:
            return
        graph_json.parent.mkdir(parents=True, exist_ok=True)
        cfg: dict = {}
        if graph_json.exists():
            try:
                cfg = json.loads(graph_json.read_text())
            except json
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[dumps]]
- [[exists]]
- [[list]]
- [[loads]]
- [[mkdir]]
- [[read_text]]
- [[write_text]]


## Called by

- [[VaultGenerator__generate]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator__generate]]
- [[dumps]]
- [[exists]]
- [[list]]
- [[loads]]
- [[mkdir]]
- [[read_text]]
- [[write_text]]

