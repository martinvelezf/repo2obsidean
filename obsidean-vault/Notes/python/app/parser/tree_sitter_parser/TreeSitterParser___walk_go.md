---
name: TreeSitterParser._walk_go
kind: method
language: python
file: app/parser/tree_sitter_parser.py
line: 248
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._walk_go
  - _walk_go
---

# _walk_go

Recursively walk the Go tree, emitting type/func/method symbols.

## Signature

```python
def _walk_go( self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _walk_go(
        self,
        node: tree_sitter.Node,
        file_path: Path,
        lines: list[str],
        symbols: list[Symbol],
    ):
        """Recursively walk the Go tree, emitting type/func/method symbols."""
        for child in node.children:
            if child.type == "type_declaration":
                for spec in child.children:
                    if spec.type == "type_spec":
                        name = self._field_text(spec, "name")
                        if name:
                            symbols.append(
                                Symbol(
                                    name=name,
                                    kind=SymbolKind.CLASS,  # struct/interface ~ class
                                    language=Language.GO,
                   
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[Symbol]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___go_doc_comment]]
- [[TreeSitterParser___go_receiver]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser___walk_go]]
- [[append]]


## Called by

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser__parse_file]]


## Related

- [[Symbol]]
- [[TreeSitterParser]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___go_doc_comment]]
- [[TreeSitterParser___go_receiver]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser__parse_file]]
- [[append]]

