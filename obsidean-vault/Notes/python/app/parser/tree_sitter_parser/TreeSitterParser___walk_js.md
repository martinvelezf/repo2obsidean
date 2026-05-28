---
name: TreeSitterParser._walk_js
kind: method
language: python
file: app/parser/tree_sitter_parser.py
line: 349
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._walk_js
  - _walk_js
---

# _walk_js

Recursively walk the JS tree, emitting class/method/function symbols.

## Signature

```python
def _walk_js( self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _walk_js(
        self,
        node: tree_sitter.Node,
        file_path: Path,
        lines: list[str],
        symbols: list[Symbol],
        scope_class: Optional[str],
    ):
        """Recursively walk the JS tree, emitting class/method/function symbols."""
        for child in node.children:
            if child.type in ("class_declaration", "class"):
                name = self._field_text(child, "name") or "<anonymous>"
                symbols.append(
                    Symbol(
                        name=name,
                        kind=SymbolKind.CLASS,
                        language=Language.JAVASCRIPT,
                        qualified_name=name,
                        file=file_path,
                        start_line=child.start_point[0] + 1,
                
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[Symbol]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___js_doc_comment]]
- [[TreeSitterParser___js_heritage]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser___walk_js]]
- [[append]]
- [[child_by_field_name]]


## Called by

- [[TreeSitterParser___walk_js]]
- [[TreeSitterParser__parse_file]]


## Related

- [[Symbol]]
- [[TreeSitterParser]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___js_doc_comment]]
- [[TreeSitterParser___js_heritage]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser__parse_file]]
- [[append]]
- [[child_by_field_name]]

