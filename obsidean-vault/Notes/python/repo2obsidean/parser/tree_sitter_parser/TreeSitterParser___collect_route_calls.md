---
name: TreeSitterParser._collect_route_calls
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 542
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._collect_route_calls
  - _collect_route_calls
---

# _collect_route_calls

Return handler names referenced by router-registration calls.

## Signature

```python
def _collect_route_calls(self, root
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _collect_route_calls(self, root: tree_sitter.Node, lang: Language) -> set[str]:
        """Return handler names referenced by router-registration calls."""
        handlers: set[str] = set()
        self._walk_route_calls(root, lang, handlers)
        return handlers
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___walk_route_calls]]
- [[set]]


## Called by

- [[TreeSitterParser__parse_file]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_route_calls]]
- [[TreeSitterParser__parse_file]]
- [[set]]

