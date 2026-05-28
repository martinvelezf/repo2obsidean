---
name: _fake_test
kind: function
language: python
file: app/cli.py
line: 28
tags: [code, python, function, changed]
changed: true
change_status: M
aliases:
  - _fake_test
  - _fake_test
---

# _fake_test

This dummy function exists to make sure the above constants are included in coverage.

#changed

> [!warning] Changed since git HEAD — status `M`

```diff
@@ -29 +28,3 @@ IGNORE_DIRS = {
-
+def _fake_test():
+    """This dummy function exists to make sure the above constants are included in coverage."""
+    pass
```

## Signature

```python
def _fake_test()
```

## Source

<details>
<summary>Show implementation</summary>

```python
def _fake_test():
    """This dummy function exists to make sure the above constants are included in coverage."""
    pass
```

</details>



## Called by

- [[_matches_any]]


## Related

- [[_matches_any]]

