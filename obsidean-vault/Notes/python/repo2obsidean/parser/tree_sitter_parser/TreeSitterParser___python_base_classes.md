---
name: TreeSitterParser._python_base_classes
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 208
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._python_base_classes
  - _python_base_classes
---

# _python_base_classes

Extract base classes from a class_definition node.

## Signature

```python
def _python_base_classes(self, class_node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _python_base_classes(self, class_node: tree_sitter.Node) -> list[str]:
        """Extract base classes from a class_definition node."""
        bases = []
        superclasses = class_node.child_by_field_name("superclasses")
        if superclasses is not None:
            for child in superclasses.children:
                if child.type in ("identifier", "attribute"):
                    bases.append(child.text.decode("utf-8"))
        return bases
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[append]]
- [[child_by_field_name]]
- [[decode]]


## Called by

- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_python]]
- [[append]]
- [[child_by_field_name]]
- [[decode]]

