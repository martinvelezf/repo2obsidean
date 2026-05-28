---
name: TreeSitterParser._js_heritage
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 448
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._js_heritage
  - _js_heritage
---

# _js_heritage

Extract the superclass from a JS `class X extends Y` declaration.

## Signature

```python
def _js_heritage(self, class_node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _js_heritage(self, class_node: tree_sitter.Node) -> list[str]:
        """Extract the superclass from a JS `class X extends Y` declaration."""
        bases = []
        for child in class_node.children:
            if child.type == "class_heritage":
                for sub in child.children:
                    if sub.type in ("identifier", "member_expression"):
                        bases.append(sub.text.decode("utf-8"))
        return bases
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[append]]
- [[decode]]


## Called by

- [[TreeSitterParser___walk_js]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_js]]
- [[append]]
- [[decode]]

