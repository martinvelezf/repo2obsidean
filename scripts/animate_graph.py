#!/usr/bin/env python
"""Render the obsidean symbol graph to an animated GIF.

Changed symbols (uncommitted vs git HEAD) pulse red; everything else is grey.
This is the animated, code-derived version of Obsidian's graph view.

Usage:
    python scripts/animate_graph.py [PATH ...] [--out docs/graph-changed.gif]
"""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # headless
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from repo2obsidean.cli import _detect_languages, _iter_source_files, _stamp_git_changes
from repo2obsidean.graph.builder import SymbolGraph
from repo2obsidean.parser.base import Language
from repo2obsidean.parser.tree_sitter_parser import TreeSitterParser


def build_graph(paths: list[Path]) -> SymbolGraph:
    """Parse the given roots, stamp git changes, and build the symbol graph."""
    roots = [(p, p.name if len(paths) > 1 else "") for p in paths]
    symbols = []
    for root, layer in roots:
        for lang in _detect_languages(root):
            parser = TreeSitterParser(lang)
            for f in _iter_source_files(root, lang):
                try:
                    symbols.extend(parser.parse_file(f, layer=layer))
                except Exception:  # noqa: BLE001
                    pass
    _stamp_git_changes(roots, symbols)
    graph = SymbolGraph()
    graph.build_from_symbols(symbols)
    return graph


def render_gif(graph: SymbolGraph, out: Path, frames: int = 48, fps: int = 16):
    """Animate the graph to a looping GIF, pulsing the changed nodes red."""
    g = graph.graph
    changed = {s.qualified_name for s in graph.all_symbols if s.changed}

    # Stable layout (seeded so reruns look the same).
    pos = nx.spring_layout(g, seed=7, k=0.9 / np.sqrt(max(len(g), 1)), iterations=60)
    xs = np.array([pos[n][0] for n in g.nodes()])
    ys = np.array([pos[n][1] for n in g.nodes()])
    is_changed = np.array([n in changed for n in g.nodes()])

    fig, ax = plt.subplots(figsize=(11, 8), dpi=110)
    fig.patch.set_facecolor("#141414")
    ax.set_facecolor("#141414")
    ax.axis("off")

    # Static edges (drawn once, behind the nodes).
    for u, v in g.edges():
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                color="#3a3a3a", linewidth=0.4, zorder=1)

    base = np.where(is_changed, 90.0, 28.0)
    grey, red = "#8a8a8a", "#ff3b30"
    colors = np.where(is_changed, red, grey)

    scat = ax.scatter(xs, ys, s=base, c=colors, zorder=2,
                      edgecolors="none", alpha=0.9)

    # Label the changed nodes so they're identifiable.
    for n in g.nodes():
        if n in changed:
            ax.annotate(n.split(".")[-1], pos[n], color="#ff6b60",
                        fontsize=7, ha="center", va="bottom", zorder=3)

    ax.set_title(f"obsidean graph — {len(changed)} changed symbol(s) in red",
                 color="#dddddd", fontsize=12)

    def update(frame):
        # Pulse only the changed nodes (sinusoidal size + alpha).
        phase = np.sin(2 * np.pi * frame / frames)
        sizes = base.copy()
        sizes[is_changed] = 90 + 130 * (0.5 + 0.5 * phase)
        scat.set_sizes(sizes)
        return (scat,)

    anim = animation.FuncAnimation(fig, update, frames=frames, blit=True)
    out.parent.mkdir(parents=True, exist_ok=True)
    anim.save(out, writer=animation.PillowWriter(fps=fps))
    plt.close(fig)
    print(f"wrote {out} ({len(g)} nodes, {len(changed)} changed)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=["app"])
    ap.add_argument("--out", default="docs/graph-changed.gif", type=Path)
    args = ap.parse_args()
    paths = [Path(p) for p in (args.paths or ["app"])]
    render_gif(build_graph(paths), args.out)


if __name__ == "__main__":
    main()
