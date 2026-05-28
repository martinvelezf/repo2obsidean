---
name: TreeSitterParser._walk_python
kind: method
language: python
file: /home/martin/lab/obsidean/app/parser/tree_sitter_parser.py
line: 52
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._walk_python
  - _walk_python
---

# _walk_python

Recursively walk the Python tree, emitting class/method/function symbols.

## Signature

```python
def _walk_python( self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _walk_python(
        self,
        node: tree_sitter.Node,
        file_path: Path,
        lines: list[str],
        symbols: list[Symbol],
        scope_class: Optional[str],
        decorators: Optional[list[str]] = None,
    ):
        """Recursively walk the Python tree, emitting class/method/function symbols."""
        for child in node.children:
            if child.type == "decorated_definition":
                # Capture decorators, then process the wrapped definition.
                decs = self._python_decorators(child)
                self._walk_python(child, file_path, lines, symbols, scope_class, decs)

            elif child.type == "class_definition":
                name = self._field_text(child, "name")
                if not name:
                    continue
 
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[Symbol]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___python_base_classes]]
- [[TreeSitterParser___python_decorators]]
- [[TreeSitterParser___python_docstring]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser___walk_python]]
- [[append]]
- [[child_by_field_name]]


## Called by

- [[TreeSitterParser___walk_python]]
- [[TreeSitterParser__parse_file]]


## Related

- [[Symbol]]
- [[TreeSitterParser]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___python_base_classes]]
- [[TreeSitterParser___python_decorators]]
- [[TreeSitterParser___python_docstring]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser__parse_file]]
- [[append]]
- [[child_by_field_name]]

