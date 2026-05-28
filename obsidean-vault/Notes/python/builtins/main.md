---
name: main
kind: function
language: python
file: /home/martin/lab/obsidean/app/cli.py
line: 73
tags: [code, python, function]
aliases:
  - main
  - main
---

# main

Turn a code repository into an Obsidian vault.

    Run with no arguments in a repo directory (like `repomix`):

        obsidean

    Or point it at a path and output location:

        obsidean ./myrepo --out ./vault
        obsidean ./myrepo -l python -l go

## Signature

```python
def main(repo_path
```

## Source

<details>
<summary>Show implementation</summary>

```python
def main(repo_path: Path, out: Path, languages: tuple[str, ...]):
    """Turn a code repository into an Obsidian vault.

    Run with no arguments in a repo directory (like `repomix`):

        obsidean

    Or point it at a path and output location:

        obsidean ./myrepo --out ./vault
        obsidean ./myrepo -l python -l go
    """
    repo = repo_path or Path.cwd()
    out = out or (Path.cwd() / "obsidean-vault")

    selected = [Language(l) for l in languages] if languages else _detect_languages(repo)
    if not selected:
        click.echo(f"No supported source files (.py/.go) found in {repo}", err=True)
        sys.exit(1)

    click.echo(f"Repo:   {repo}")
    click.echo(f"Output: {out}")
    click.echo(f"Languages: {', '.join(l.value for l in selected)}")

    count = _build_
```

</details>

## Decorators

- `@click.command()`
- `@click.argument("repo_path", required=False, type=click.Path(exists=True, path_type=Path))`
- `@click.option("--out", "-o", type=click.Path(path_type=Path), default=None,
              help="Output vault directory (default: ./obsidean-vault)")`
- `@click.option("--language", "-l", "languages", multiple=True,
              type=click.Choice([l.value for l in Language]),
              help="Limit to specific language(s). Repeatable. Default: auto-detect.")`
- `@click.version_option(package_name="obsidean")`


## Calls

- [[Language]]
- [[_build_vault]]
- [[_detect_languages]]
- [[cwd]]
- [[echo]]
- [[exit]]
- [[join]]



## Related

- [[Language]]
- [[_build_vault]]
- [[_detect_languages]]
- [[cwd]]
- [[echo]]
- [[exit]]
- [[join]]

