---
name: TreeSitterParser._go_receiver
kind: method
language: python
file: /home/martin/lab/obsidean/app/parser/tree_sitter_parser.py
line: 237
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._go_receiver
  - _go_receiver
---

# _go_receiver

Extract the receiver type of a Go method (e.g. '*Service' -> 'Service').

## Signature

```python
def _go_receiver(self, method_node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _go_receiver(self, method_node: tree_sitter.Node) -> Optional[str]:
        """Extract the receiver type of a Go method (e.g. '*Service' -> 'Service')."""
        receiver = method_node.child_by_field_name("receiver")
        if receiver is None:
            return None
        for param in receiver.children:
            if param.type == "parameter_declaration":
                type_node = param.child_by_field_name("type")
                if type_node is not None:
                    return type_node.text.decode("utf-8").lstrip("*")
        return None
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[child_by_field_name]]
- [[decode]]
- [[lstrip]]


## Called by

- [[TreeSitterParser___walk_go]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_go]]
- [[child_by_field_name]]
- [[decode]]
- [[lstrip]]

