---
name: TreeSitterParser.apply_route_tags
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 101
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser.apply_route_tags
  - apply_route_tags
---

# apply_route_tags

Tag any symbol whose name matches a collected route handler.

        Run after all files are parsed so route registrations in one file tag
        handler functions defined in another.

## Signature

```python
def apply_route_tags(self, symbols
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def apply_route_tags(self, symbols: list[Symbol]) -> None:
        """Tag any symbol whose name matches a collected route handler.

        Run after all files are parsed so route registrations in one file tag
        handler functions defined in another.
        """
        if not self.route_handlers:
            return
        for s in symbols:
            if (s.language == self.language and not s.is_route
                    and s.kind in (SymbolKind.FUNCTION, SymbolKind.METHOD)
                    and s.name in self.route_handlers):
                s.is_route = True
```

</details>


## Parent

- [[TreeSitterParser]]




## Related

- [[TreeSitterParser]]

