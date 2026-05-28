---
name: SymbolGraph.build_from_symbols
kind: method
language: python
file: app/graph/builder.py
line: 40
tags: [code, python, method]
parent: "[[SymbolGraph]]"
aliases:
  - SymbolGraph.build_from_symbols
  - build_from_symbols
---

# build_from_symbols

Build the graph from a list of parsed symbols.

## Signature

```python
def build_from_symbols(self, symbols
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def build_from_symbols(self, symbols: list[Symbol]):
        """Build the graph from a list of parsed symbols."""
        self.all_symbols = list(symbols)

        # Add all symbols as nodes
        for symbol in symbols:
            self.add_symbol(symbol)

        # Build relationships
        for symbol in symbols:
            # Parent relationships (inheritance)
            for parent in symbol.parents:
                # Try to resolve parent in same module
                parent_qualified = self._resolve_name(parent, symbol.qualified_name)
                if parent_qualified in self.symbols:
                    self.add_edge(symbol.qualified_name, parent_qualified, "INHERITS")

            # Call relationships
            for call in symbol.calls:
                call_qualified = 
```

</details>


## Parent

- [[SymbolGraph]]


## Calls

- [[SymbolGraph___build_odoo_index]]
- [[SymbolGraph___resolve_call]]
- [[SymbolGraph___resolve_name]]
- [[SymbolGraph__add_edge]]
- [[SymbolGraph__add_symbol]]
- [[add_node]]
- [[list]]



## Related

- [[SymbolGraph]]
- [[SymbolGraph___build_odoo_index]]
- [[SymbolGraph___resolve_call]]
- [[SymbolGraph___resolve_name]]
- [[SymbolGraph__add_edge]]
- [[SymbolGraph__add_symbol]]
- [[add_node]]
- [[list]]

