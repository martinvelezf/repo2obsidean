"""Tests for route/endpoint detection and the #route tag."""

from pathlib import Path

import pytest

from repo2obsidean.parser.base import Language
from repo2obsidean.parser.tree_sitter_parser import TreeSitterParser, is_route_decorator


@pytest.mark.parametrize("decorators,expected", [
    (['app.get("/x")'], True),
    (['router.post("/x")'], True),
    (['app.route("/x")'], True),
    (['http.route("/web", auth="public")'], True),
    (['route("/api")'], True),
    (['app.websocket("/ws")'], True),
    (['staticmethod'], False),
    (['property'], False),
    (['get'], False),          # bare verb, ambiguous -> not a route
    ([], False),
])
def test_is_route_decorator(decorators, expected):
    assert is_route_decorator(decorators) is expected


def test_routes_flagged_in_fixture():
    f = Path(__file__).parent.parent / "fixtures" / "routes.py"
    symbols = {s.name: s for s in TreeSitterParser(Language.PYTHON).parse_file(f)}

    for name in ("list_items", "create_item", "health", "web_login", "api_data"):
        assert symbols[name].is_route, f"{name} should be a route"

    for name in ("helper", "value", "plain_function"):
        assert not symbols[name].is_route, f"{name} should NOT be a route"


def test_go_routes_via_registration_calls():
    f = Path(__file__).parent.parent / "fixtures" / "go_routes.go"
    symbols = {s.name: s for s in TreeSitterParser(Language.GO).parse_file(f)}

    # Registered via http.HandleFunc / r.GET / r.POST (same file).
    for name in ("listUsers", "createUser", "healthCheck"):
        assert symbols[name].is_route, f"{name} should be a route"
    assert not symbols["helper"].is_route


def test_js_routes_via_registration_calls():
    f = Path(__file__).parent.parent / "fixtures" / "js_routes.js"
    symbols = {s.name: s for s in TreeSitterParser(Language.JAVASCRIPT).parse_file(f)}

    for name in ("listUsers", "createUser"):
        assert symbols[name].is_route, f"{name} should be a route"
    assert not symbols["notARoute"].is_route
