"""Detect uncommitted working-tree changes via git and map them to symbols.

Everything here is read-only (status/diff). If a path is not inside a git
repository, the functions degrade gracefully to "no changes".
"""

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Hunk:
    """A unified-diff hunk, located by its line range in the new file."""

    new_start: int
    new_end: int
    text: str


@dataclass
class ChangeInfo:
    """Working-tree change state for a single file."""

    status: str  # "M" | "A" | "D"
    hunks: list[Hunk] = field(default_factory=list)


_HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    """Run a git command in ``root`` and capture output (never raises)."""
    try:
        return subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        # git not installed
        return subprocess.CompletedProcess(args, 1, "", "git not found")


def is_git_repo(root: Path) -> bool:
    """True if ``root`` is inside a git working tree."""
    r = _git(root, "rev-parse", "--is-inside-work-tree")
    return r.returncode == 0 and r.stdout.strip() == "true"


def get_working_tree_changes(root: Path) -> dict[Path, ChangeInfo]:
    """Return {resolved_file_path: ChangeInfo} for uncommitted changes.

    Combines staged + unstaged + untracked, i.e. everything that differs from
    HEAD in the working tree.
    """
    if not is_git_repo(root):
        return {}

    top = _git(root, "rev-parse", "--show-toplevel").stdout.strip()
    repo_top = Path(top) if top else Path(root)

    changes: dict[Path, ChangeInfo] = {}

    # 1) Which files changed (incl. untracked) and their coarse status.
    status = _git(root, "status", "--porcelain", "--untracked-files=all").stdout
    for line in status.splitlines():
        if not line.strip():
            continue
        code = line[:2]
        rest = line[3:]
        if " -> " in rest:  # rename: take the new path
            rest = rest.split(" -> ")[-1]
        path = (repo_top / rest.strip()).resolve()
        if code == "??":
            changes[path] = ChangeInfo(status="A")          # untracked / new
        elif "D" in code:
            changes[path] = ChangeInfo(status="D")
        else:
            changes[path] = ChangeInfo(status="M")

    # 2) Per-file hunks for tracked modifications (working tree vs HEAD).
    #    -U0 (zero context) so a hunk's line range covers only *changed* lines,
    #    giving precise symbol overlap instead of bleeding into neighbours.
    diff_text = _git(root, "diff", "HEAD", "-U0").stdout
    for file_path, hunks in _parse_unified_diff(diff_text, repo_top).items():
        if file_path in changes:
            changes[file_path].hunks = hunks
        else:
            changes[file_path] = ChangeInfo(status="M", hunks=hunks)

    return changes


def _parse_unified_diff(diff_text: str, repo_top: Path) -> dict[Path, list[Hunk]]:
    """Parse `git diff` output into {file_path: [Hunk, ...]}."""
    files: dict[Path, list[Hunk]] = {}
    current_file: Path | None = None
    current_hunk: Hunk | None = None
    hunk_lines: list[str] = []

    def flush_hunk():
        nonlocal current_hunk, hunk_lines
        if current_file is not None and current_hunk is not None:
            current_hunk.text = "\n".join(hunk_lines)[:1200]
            files.setdefault(current_file, []).append(current_hunk)
        current_hunk = None
        hunk_lines = []

    for line in diff_text.splitlines():
        if line.startswith("diff --git"):
            # New file section — close any open hunk, reset file until +++.
            flush_hunk()
            current_file = None
        elif line.startswith("--- "):
            flush_hunk()
        elif line.startswith("+++ "):
            flush_hunk()
            rel = line[len("+++ "):].strip()
            if rel.startswith("b/"):
                rel = rel[2:]
            current_file = (repo_top / rel).resolve() if rel and rel != "/dev/null" else None
        elif line.startswith("@@"):
            flush_hunk()
            m = _HUNK_RE.match(line)
            if m and current_file is not None:
                new_start = int(m.group(1))
                new_count = int(m.group(2)) if m.group(2) else 1
                # A zero-line hunk (pure deletion) still anchors at new_start.
                new_end = new_start + max(new_count, 1) - 1
                current_hunk = Hunk(new_start=new_start, new_end=new_end, text="")
                hunk_lines = [line]
        elif current_hunk is not None:
            hunk_lines.append(line)

    flush_hunk()
    return files


def diff_for_lines(info: ChangeInfo, start_line: int, end_line: int) -> str:
    """Return the diff hunks overlapping a symbol's [start_line, end_line]."""
    if info.status == "A":
        return "(new file — not yet committed)"
    if info.status == "D":
        return "(file deleted)"
    overlapping = [
        h.text for h in info.hunks
        if h.new_start <= end_line and h.new_end >= start_line
    ]
    return "\n".join(overlapping)[:1500]
