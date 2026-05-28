---
name: VaultGenerator._generate_recent_changes
kind: method
language: python
file: app/generator/vault.py
line: 174
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._generate_recent_changes
  - _generate_recent_changes
---

# _generate_recent_changes

Write an index of symbols whose source changed since git HEAD.

## Signature

```python
def _generate_recent_changes(self, graph
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _generate_recent_changes(self, graph: SymbolGraph):
        """Write an index of symbols whose source changed since git HEAD."""
        changed = [s for s in graph.all_symbols if s.changed]
        if not changed:
            return

        status_label = {"M": "modified", "A": "added", "D": "deleted"}
        lines = [
            "---",
            "tags: [obsidean, recent-changes]",
            "---",
            "",
            "# Recent Changes",
            "",
            f"{len(changed)} symbol(s) changed in the working tree since git HEAD.",
            "",
        ]

        # Group by layer, then by file.
        by_layer: dict[str, dict[str, list[Symbol]]] = {}
        for s in changed:
            by_layer.setdefault(s.layer or "root", {}).setdefault(str(s.file), [])
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[VaultGenerator___symbol_link]]
- [[append]]
- [[get]]
- [[join]]
- [[len]]
- [[setdefault]]
- [[sorted]]
- [[str]]
- [[write_text]]


## Called by

- [[VaultGenerator__generate]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator___symbol_link]]
- [[VaultGenerator__generate]]
- [[append]]
- [[get]]
- [[join]]
- [[len]]
- [[setdefault]]
- [[sorted]]
- [[str]]
- [[write_text]]

