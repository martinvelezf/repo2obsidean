---
name: VaultGenerator._generate_odoo_report
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 164
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._generate_odoo_report
  - _generate_odoo_report
---

# _generate_odoo_report

Write an Odoo model-inheritance report, including the dangling check.

        Skipped entirely when the codebase has no Odoo models.

## Signature

```python
def _generate_odoo_report(self, graph
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _generate_odoo_report(self, graph: SymbolGraph):
        """Write an Odoo model-inheritance report, including the dangling check.

        Skipped entirely when the codebase has no Odoo models.
        """
        if not graph.odoo_models:
            return

        lines = ["# Odoo Model Inheritance", ""]

        unresolved = graph.odoo_unresolved
        if unresolved:
            lines.append("## ⚠️ Unresolved inherits")
            lines.append("")
            lines.append("Models referenced via `_inherit`/`_inherits` but **never "
                         "defined** in the scanned roots (likely a missing addon tree):")
            lines.append("")
            for model in sorted(unresolved):
                referrers = unresolved[model]
                layers = sorted({s.lay
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[append]]
- [[join]]
- [[len]]
- [[sorted]]
- [[write_text]]


## Called by

- [[VaultGenerator__generate]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator__generate]]
- [[append]]
- [[join]]
- [[len]]
- [[sorted]]
- [[write_text]]

