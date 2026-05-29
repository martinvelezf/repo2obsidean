// Express-style route registrations.

function listUsers(req, res) {
    res.json([]);
}

function createUser(req, res) {
    res.json({});
}

function notARoute(x) {
    return x + 1;
}

const app = express();
app.get("/users", listUsers);
router.post("/users", createUser);
app.get("/inline", (req, res) => res.end());   // anonymous -> not tagged
