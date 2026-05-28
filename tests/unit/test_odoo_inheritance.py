"""Tests for Odoo model extraction and cross-layer inheritance checking."""

from pathlib import Path

import pytest

from repo2obsidean.graph.builder import SymbolGraph
from repo2obsidean.parser.base import Language
from repo2obsidean.parser.tree_sitter_parser import TreeSitterParser


@pytest.fixture
def odoo_symbols():
    f = Path(__file__).parent.parent / "fixtures" / "odoo_models.py"
    return TreeSitterParser(Language.PYTHON).parse_file(f, layer="odoo")


def test_extracts_odoo_attrs(odoo_symbols):
    by_name = {s.name: s for s in odoo_symbols}
    assert by_name["SaleOrderBase"].odoo_model == "sale.order"
    assert by_name["SaleOrderExtension"].odoo_inherit == ["sale.order"]
    assert by_name["ResPartner"].odoo_inherit == ["res.partner", "mail.thread"]
    assert by_name["ResPartner"].odoo_inherits == ["res.company"]


def test_layer_stamped(odoo_symbols):
    assert all(s.layer == "odoo" for s in odoo_symbols)


def test_model_index_and_unresolved(odoo_symbols):
    graph = SymbolGraph()
    graph.build_from_symbols(odoo_symbols)

    # sale.order is defined (base) and extended -> resolved.
    assert "sale.order" in graph.odoo_models
    assert graph.odoo_models["sale.order"]["bases"], "expected a base definition"
    assert graph.odoo_models["sale.order"]["extensions"], "expected an extension"
    assert "sale.order" not in graph.odoo_unresolved

    # res.partner / mail.thread / res.company have no base here -> unresolved.
    assert "res.partner" in graph.odoo_unresolved
    assert "mail.thread" in graph.odoo_unresolved
    assert "res.company" in graph.odoo_unresolved
