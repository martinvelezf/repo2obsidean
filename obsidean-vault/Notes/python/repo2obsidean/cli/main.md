---
name: main
kind: function
language: python
file: repo2obsidean/cli.py
line: 170
tags: [code, python, function]
aliases:
  - main
  - main
---

# main

Turn one or more code repositories into a single Obsidian vault.

    Run with no arguments in a repo directory (like `repomix`):

        obsidean

    Point it at a path, or at several addon trees at once (e.g. Odoo):

        obsidean ./myrepo --out ./vault
        obsidean ./odoo ./user ./enterprise --out ./vault       # multi-layer
        obsidean --layer odoo=./odoo --layer user=./custom      # explicit names

    Filter which directories/files are scanned:

        obsidean . --include '

## Signature

```python
def main(repo_paths
```

## Source

<details>
<summary>Show implementation</summary>

```python
def main(repo_paths: tuple[Path, ...], out: Path, languages: tuple[str, ...],
         include: tuple[str, ...], exclude: tuple[str, ...],
         layer_maps: tuple[str, ...], use_git: bool, reset_graph_config: bool):
    """Turn one or more code repositories into a single Obsidian vault.

    Run with no arguments in a repo directory (like `repomix`):

        obsidean

    Point it at a path, or at several addon trees at once (e.g. Odoo):

        obsidean ./myrepo --out ./vault
        obsidean ./odoo ./user ./enterprise --out ./vault       # multi-layer
        obsidean --layer odoo=./odoo --layer user=./custom      # explicit names

    Filter which directories/files are scanned:

        obsidean . --include 'models/**' --include '*.py'
        obsidean . --exclude 'tests/**' --excl
```

</details>

## Decorators

- `@click.command()`
- `@click.argument("repo_paths", nargs=-1, type=click.Path(exists=True, path_type=Path))`
- `@click.option("--out", "-o", type=click.Path(path_type=Path), default=None,
              help="Output vault directory (default: ./obsidean-vault)")`
- `@click.option("--language", "-l", "languages", multiple=True,
              type=click.Choice([l.value for l in Language]),
              help="Limit to specific language(s). Repeatable. Default: auto-detect.")`
- `@click.option("--include", "include", multiple=True, metavar="GLOB",
              help="Only include files matching this glob (repeatable).")`
- `@click.option("--exclude", "exclude", multiple=True, metavar="GLOB",
              help="Exclude files matching this glob (repeatable).")`
- `@click.option("--layer", "layer_maps", multiple=True, metavar="NAME=PATH",
              help="Map an explicit layer name to a directory (repeatable).")`
- `@click.option("--git/--no-git", "use_git", default=True,
              help="Detect uncommitted working-tree changes and flag them (default: on).")`
- `@click.option("--reset-graph-config", "reset_graph_config", is_flag=True, default=False,
              help="Re-seed the default colour groups in .obsidian/graph.json (overwrites "
                   "existing groups while preserving other display/forces settings).")`
- `@click.version_option(package_name="repo2obsidean")`


## Calls

- [[Language]]
- [[Path]]
- [[_build_vault]]
- [[_detect_languages]]
- [[append]]
- [[cwd]]
- [[echo]]
- [[exists]]
- [[exit]]
- [[expanduser]]
- [[join]]
- [[len]]
- [[list]]
- [[partition]]
- [[repr]]
- [[sorted]]
- [[str]]
- [[strip]]
- [[values]]



## Related

- [[Language]]
- [[Path]]
- [[_build_vault]]
- [[_detect_languages]]
- [[append]]
- [[cwd]]
- [[echo]]
- [[exists]]
- [[exit]]
- [[expanduser]]
- [[join]]
- [[len]]
- [[list]]
- [[partition]]
- [[repr]]
- [[sorted]]
- [[str]]
- [[strip]]
- [[values]]

