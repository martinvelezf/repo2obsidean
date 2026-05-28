---
name: TreeSitterParser._python_docstring
kind: method
language: python
file: app/parser/tree_sitter_parser.py
line: 228
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._python_docstring
  - _python_docstring
---

# _python_docstring

Extract the docstring (first string literal in the body).

## Signature

```python
def _python_docstring(self, def_node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _python_docstring(self, def_node: tree_sitter.Node) -> str:
        """Extract the docstring (first string literal in the body)."""
        body = def_node.child_by_field_name("body")
        if body is None:
            return ""
        for stmt in body.children:
            if stmt.type == "expression_statement":
                for expr in stmt.children:
                    if expr.type == "string":
                        raw = expr.text.decode("utf-8")
                        return self._clean_docstring(raw)
            # Only the first statement can be a docstring.
            if stmt.type not in ("comment",):
                break
        return ""
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___clean_docstring]]
- [[child_by_field_name]]
- [[decode]]


## Called by

- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___clean_docstring]]
- [[TreeSitterParser___walk_python]]
- [[child_by_field_name]]
- [[decode]]

