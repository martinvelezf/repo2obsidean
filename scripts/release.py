#!/usr/bin/env python
"""Release a new version of repo2obsidean to PyPI.

Bumps ``version`` in pyproject.toml, runs the unit tests, builds the wheel
and sdist, validates them with twine, uploads to PyPI (or TestPyPI), and
finally tags the commit.

Usage:
    scripts/release.py                             # default: auto-bump the patch
    scripts/release.py 0.2.0                       # explicit new version
    scripts/release.py --bump minor                # auto-bump minor (or major/patch)
    scripts/release.py --testpypi                  # publish to TestPyPI instead
    scripts/release.py --build-only                # bump + build, skip upload
    scripts/release.py -y                          # skip the confirm prompt

Requires `build` and `twine` (``pip install build twine``).

Credentials: set TWINE_USERNAME=__token__  TWINE_PASSWORD=pypi-...  in your env,
or configure ``~/.pypirc``. Never commit the token.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PYPROJECT = ROOT / "pyproject.toml"
DIST = ROOT / "dist"

VERSION_RE = re.compile(r'^version\s*=\s*"([^"]+)"', re.MULTILINE)
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def run(cmd: list[str], check: bool = True, cwd: Path = ROOT) -> int:
    print(f"$ {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=cwd)
    if check and proc.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd)}")
    return proc.returncode


def read_version() -> str:
    m = VERSION_RE.search(PYPROJECT.read_text())
    if not m:
        sys.exit("could not find `version = \"...\"` in pyproject.toml")
    return m.group(1)


def write_version(new: str) -> None:
    text = PYPROJECT.read_text()
    text2, n = VERSION_RE.subn(f'version = "{new}"', text, count=1)
    if n != 1:
        sys.exit("failed to substitute version in pyproject.toml")
    PYPROJECT.write_text(text2)


def bump(current: str, kind: str) -> str:
    if not SEMVER_RE.match(current):
        sys.exit(f"--bump only works on semver (X.Y.Z); current is {current!r}")
    major, minor, patch = (int(x) for x in current.split("."))
    if kind == "major":
        return f"{major + 1}.0.0"
    if kind == "minor":
        return f"{major}.{minor + 1}.0"
    if kind == "patch":
        return f"{major}.{minor}.{patch + 1}"
    sys.exit(f"unknown bump kind: {kind}")


def git_clean() -> bool:
    r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=ROOT)
    return r.returncode == 0 and not r.stdout.strip()


def git(*args: str) -> None:
    run(["git", *args])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("version", nargs="?",
                    help="explicit new version, e.g. 0.2.0; omit to auto-bump the patch")
    ap.add_argument("--bump", choices=["major", "minor", "patch"],
                    help="auto-bump kind when no explicit version is given (default: patch)")
    ap.add_argument("--testpypi", action="store_true", help="upload to TestPyPI instead of PyPI")
    ap.add_argument("--build-only", action="store_true", help="bump + build; skip upload + tag")
    ap.add_argument("--skip-tests", action="store_true", help="skip running pytest")
    ap.add_argument("--skip-tag", action="store_true", help="don't git commit/tag after upload")
    ap.add_argument("--allow-dirty", action="store_true", help="proceed even if working tree is dirty")
    ap.add_argument("-y", "--yes", action="store_true", help="don't prompt before uploading")
    args = ap.parse_args()

    if args.version and args.bump:
        ap.error("choose either an explicit version OR --bump, not both")
    if args.version and not SEMVER_RE.match(args.version):
        ap.error(f"version must be semver (X.Y.Z), got {args.version!r}")

    current = read_version()
    if args.version:
        new = args.version
    else:
        # Default: auto-bump the patch number when no version is supplied.
        new = bump(current, args.bump or "patch")
    if new == current:
        sys.exit(f"new version is the same as current ({current}) — PyPI won't accept it")
    print(f"current: {current}  →  new: {new}")

    if not git_clean() and not args.allow_dirty and not args.build_only:
        sys.exit("working tree is dirty; commit/stash first, or pass --allow-dirty")

    if not args.skip_tests:
        run([sys.executable, "-m", "pytest", "tests/unit", "-q"])

    # 1. Bump version in pyproject.toml.
    write_version(new)
    print(f"updated pyproject.toml: version = {new}")

    # 2. Clean & build wheel + sdist.
    if DIST.exists():
        shutil.rmtree(DIST)
    run([sys.executable, "-m", "build"])

    # 3. Validate metadata.
    dist_files = sorted(str(p) for p in DIST.iterdir() if p.suffix in (".whl", ".gz"))
    if not dist_files:
        sys.exit("no artifacts in dist/")
    run([sys.executable, "-m", "twine", "check", *dist_files])

    if args.build_only:
        print(f"\n✓ built {len(dist_files)} artifact(s) in dist/  (version {new}) — upload skipped")
        return

    target = "TestPyPI" if args.testpypi else "PyPI"
    if not args.yes:
        ans = input(f"\nUpload to {target}? [y/N] ").strip().lower()
        if ans not in ("y", "yes"):
            print("aborted (pyproject.toml was bumped; "
                  "revert with: git checkout -- pyproject.toml)")
            sys.exit(1)

    # 4. Upload.
    upload = [sys.executable, "-m", "twine", "upload"]
    if args.testpypi:
        upload += ["--repository", "testpypi"]
    upload += dist_files
    run(upload)

    # 5. Commit + tag (only on real PyPI release, not TestPyPI rehearsals).
    if not args.skip_tag and not args.testpypi:
        git("add", "pyproject.toml")
        git("commit", "-m", f"Release {new}")
        git("tag", f"v{new}", "-m", f"Release {new}")
        print(f"  tagged v{new} — push with: git push && git push --tags")

    install_cmd = "pip install"
    if args.testpypi:
        install_cmd += " -i https://test.pypi.org/simple/"
    print(f"\n✓ repo2obsidean {new} uploaded to {target}")
    print(f"  install:  {install_cmd} repo2obsidean=={new}")


if __name__ == "__main__":
    main()
