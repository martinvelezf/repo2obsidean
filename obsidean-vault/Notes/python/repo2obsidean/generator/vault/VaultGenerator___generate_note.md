---
name: VaultGenerator._generate_note
kind: method
language: python
file: repo2obsidean/generator/vault.py
line: 66
tags: [code, python, method]
parent: "[[VaultGenerator]]"
aliases:
  - VaultGenerator._generate_note
  - _generate_note
---

# _generate_note

Generate a markdown note for a symbol.

## Signature

```python
def _generate_note(self, symbol
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _generate_note(self, symbol: Symbol, graph: SymbolGraph):
        """Generate a markdown note for a symbol."""
        # slug already includes the "Notes/" prefix, so join to output_dir.
        slug = slug_from_symbol(symbol)
        note_path = self.output_dir / slug
        note_path = self._unique_path(note_path)
        note_path.parent.mkdir(parents=True, exist_ok=True)

        # Prepare context for template
        callers = graph.get_callers(symbol.qualified_name)
        callees = graph.get_callees(symbol.qualified_name)

        context = {
            "symbol": symbol,
            "callers": self._format_links(callers),
            "callees": self._format_links(callees),
            "related": self._format_links(graph.get_related_symbols(symbol.qualified_name)),
       
```

</details>


## Parent

- [[VaultGenerator]]


## Calls

- [[VaultGenerator___format_links]]
- [[VaultGenerator___unique_path]]
- [[get_callees]]
- [[get_callers]]
- [[get_related_symbols]]
- [[get_template]]
- [[mkdir]]
- [[render]]
- [[slug_from_symbol]]
- [[write_text]]


## Called by

- [[VaultGenerator__generate]]


## Related

- [[VaultGenerator]]
- [[VaultGenerator___format_links]]
- [[VaultGenerator___unique_path]]
- [[VaultGenerator__generate]]
- [[get_callees]]
- [[get_callers]]
- [[get_related_symbols]]
- [[get_template]]
- [[mkdir]]
- [[render]]
- [[slug_from_symbol]]
- [[write_text]]

