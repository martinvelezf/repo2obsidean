---
name: TreeSitterParser._walk_route_calls
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 548
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._walk_route_calls
  - _walk_route_calls
---

# _walk_route_calls



## Signature

```python
def _walk_route_calls(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _walk_route_calls(self, node: tree_sitter.Node, lang: Language, handlers: set[str]):
        if node.type in ("call_expression", "call"):
            name = self._route_handler_name(node, lang)
            if name:
                handlers.add(name)
        for child in node.children:
            self._walk_route_calls(child, lang, handlers)
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___route_handler_name]]
- [[TreeSitterParser___walk_route_calls]]
- [[add]]


## Called by

- [[TreeSitterParser___collect_route_calls]]
- [[TreeSitterParser___walk_route_calls]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___collect_route_calls]]
- [[TreeSitterParser___route_handler_name]]
- [[add]]

