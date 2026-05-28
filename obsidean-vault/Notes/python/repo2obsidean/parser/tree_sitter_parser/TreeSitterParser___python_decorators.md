---
name: TreeSitterParser._python_decorators
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 138
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._python_decorators
  - _python_decorators
---

# _python_decorators

Extract decorator names from a decorated_definition node.

## Signature

```python
def _python_decorators(self, decorated_node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _python_decorators(self, decorated_node: tree_sitter.Node) -> list[str]:
        """Extract decorator names from a decorated_definition node."""
        decorators = []
        for child in decorated_node.children:
            if child.type == "decorator":
                text = child.text.decode("utf-8").strip().lstrip("@").strip()
                decorators.append(text)
        return decorators
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[append]]
- [[decode]]
- [[lstrip]]
- [[strip]]


## Called by

- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_python]]
- [[append]]
- [[decode]]
- [[lstrip]]
- [[strip]]

