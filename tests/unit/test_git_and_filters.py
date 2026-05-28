"""Tests for include/exclude filtering and git diff hunk parsing."""

from pathlib import Path

from repo2obsidean.cli import _matches_any, _iter_source_files
from repo2obsidean.git_utils import ChangeInfo, Hunk, diff_for_lines, _parse_unified_diff
from repo2obsidean.parser.base import Language


def test_matches_any_basename_and_relpath():
    assert _matches_any("models/sale.py", "sale.py", ("*.py",))
    assert _matches_any("models/sale.py", "sale.py", ("models/*",))
    assert not _matches_any("views/sale.xml", "sale.xml", ("*.py",))


def test_matches_any_midpath_directory():
    # `models/**` should target a models dir at any depth (Odoo layout).
    assert _matches_any("sale/models/sale_order.py", "sale_order.py", ("models/**",))
    assert _matches_any("a/b/c/tests/test_x.py", "test_x.py", ("tests/**",))
    assert not _matches_any("sale/views/order.xml", "order.xml", ("models/**",))


def test_include_exclude_filtering(tmp_path: Path):
    (tmp_path / "models").mkdir()
    (tmp_path / "tests").mkdir()
    (tmp_path / "models" / "a.py").write_text("x = 1\n")
    (tmp_path / "tests" / "b.py").write_text("y = 2\n")

    included = {p.name for p in _iter_source_files(
        tmp_path, Language.PYTHON, include=("models/**",))}
    assert included == {"a.py"}

    excluded = {p.name for p in _iter_source_files(
        tmp_path, Language.PYTHON, exclude=("tests/**",))}
    assert excluded == {"a.py"}


def test_parse_unified_diff_line_ranges():
    diff = (
        "diff --git a/foo.py b/foo.py\n"
        "index 111..222 100644\n"
        "--- a/foo.py\n"
        "+++ b/foo.py\n"
        "@@ -10,3 +10,4 @@ def foo():\n"
        " a\n"
        "+b\n"
        " c\n"
        " d\n"
    )
    parsed = _parse_unified_diff(diff, Path("/repo"))
    key = Path("/repo/foo.py").resolve()
    assert key in parsed
    hunk = parsed[key][0]
    assert hunk.new_start == 10
    assert hunk.new_end == 13


def test_diff_for_lines_overlap():
    info = ChangeInfo(status="M", hunks=[
        Hunk(new_start=10, new_end=13, text="@@ hunk-A @@"),
        Hunk(new_start=50, new_end=52, text="@@ hunk-B @@"),
    ])
    # Symbol spanning lines 12-20 overlaps only hunk-A.
    out = diff_for_lines(info, 12, 20)
    assert "hunk-A" in out and "hunk-B" not in out


def test_diff_for_lines_new_file():
    assert "new file" in diff_for_lines(ChangeInfo(status="A"), 1, 5)
