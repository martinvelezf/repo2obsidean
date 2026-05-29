---
name: VaultGenerator._format_links
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 254
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._format_links
  - _format_links
---

# _format_links

Format a list of qualified names as Obsidian wikilinks.

## Signature

```python
def _format_links(self, qualified_names
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _format_links(self, qualified_names: list[str]) -> str:
        """Format a list of qualified names as Obsidian wikilinks."""
        if not qualified_names:
            return ""

        lines = []
        for qname in sorted(set(qualified_names)):
            if not qname.startswith("?"):
                # Extract the last component for the link text
                parts = qname.split(".")
                link_text = f"{parts[-2]}__{parts[-1]}" if len(parts) >= 2 and parts[-2][0].isupper() else parts[-1]
                lines.append(f"- [[{link_text}]]")

        return "\n".join(lines) if lines else "_none_"
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[append]]
- [[isupper]]
- [[join]]
- [[len]]
- [[set]]
- [[sorted]]
- [[split]]
- [[startswith]]


## Called by

- [[VaultGenerator___generate_note]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator___generate_note]]
- [[append]]
- [[isupper]]
- [[join]]
- [[len]]
- [[set]]
- [[sorted]]
- [[split]]
- [[startswith]]

