---
name: TreeSitterParser._python_odoo_attrs
kind: method
language: python
file: app/parser/tree_sitter_parser.py
line: 157
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._python_odoo_attrs
  - _python_odoo_attrs
---

# _python_odoo_attrs

Extract Odoo `_name`, `_inherit`, `_inherits` from a class body.

        These class-body assignments — not Python base classes — are how Odoo
        models relate to each other across addon trees.

## Signature

```python
def _python_odoo_attrs( self, class_node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _python_odoo_attrs(
        self, class_node: tree_sitter.Node
    ) -> tuple[Optional[str], list[str], list[str]]:
        """Extract Odoo `_name`, `_inherit`, `_inherits` from a class body.

        These class-body assignments — not Python base classes — are how Odoo
        models relate to each other across addon trees.
        """
        model_name: Optional[str] = None
        inherit: list[str] = []
        inherits: list[str] = []

        body = class_node.child_by_field_name("body")
        if body is None:
            return model_name, inherit, inherits

        for stmt in body.children:
            if stmt.type != "expression_statement":
                continue
            for assign in stmt.children:
                if assign.type != "assignment":
                
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___collect_strings]]
- [[TreeSitterParser___dict_keys]]
- [[TreeSitterParser___str_value]]
- [[child_by_field_name]]
- [[decode]]


## Called by

- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___collect_strings]]
- [[TreeSitterParser___dict_keys]]
- [[TreeSitterParser___str_value]]
- [[TreeSitterParser___walk_python]]
- [[child_by_field_name]]
- [[decode]]

