"""Sample route handlers across frameworks for route-detection testing."""


# FastAPI-style
@app.get("/items")
def list_items():
    return []


@router.post("/items")
def create_item():
    return {}


# Flask-style
@app.route("/health")
def health():
    return "ok"


# Odoo-style
@http.route("/web/login", auth="public")
def web_login():
    return None


# Bare odoo route import
@route("/api/data")
def api_data():
    return {}


# NOT a route — plain decorator / property
@staticmethod
def helper():
    return 1


@property
def value():
    return 2


def plain_function():
    return 3
