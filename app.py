"""ACEest Fitness & Gym Flask API application"""
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

DB = "aceest_fitness.db"

# ---------- DATABASE HELPER ----------

def get_db():
    """Return a SQLite3 connection with row factory as dict"""
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database and create clients table if it doesn't exist"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            height REAL,
            weight REAL
        )
    """)
    conn.commit()
    conn.close()

# Initialize DB at app startup
init_db()

# ---------- HOME ----------

@app.route("/")
def home():
    """Return welcome message and available API endpoints"""
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym API",
        "endpoints": [
            "/programs",
            "/program/<name>",
            "/clients",
            "/add-client",
            "/bmi"
        ]
    })

# ---------- PROGRAM DATA ----------

programs = {
    "fat_loss": {
        "workout": "3 day fat loss training",
        "diet": "2000 kcal high protein diet"
    },
    "muscle_gain": {
        "workout": "Push Pull Legs hypertrophy",
        "diet": "3200 kcal muscle gain diet"
    },
    "beginner": {
        "workout": "Beginner full body program",
        "diet": "Balanced diet"
    }
}

@app.route("/programs")
def get_programs():
    """Return list of available programs"""
    return jsonify(programs)

@app.route("/program/<name>")
def get_program(name):
    """Return details of a specific program by name"""
    program = programs.get(name.lower())
    if not program:
        return jsonify({"error": "Program not found"}), 404
    return jsonify(program)

# ---------- CLIENT DATABASE ----------

@app.route("/clients")
def get_clients():
    """Return list of all clients in database"""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    rows = cur.fetchall()
    clients = [dict(row) for row in rows]
    conn.close()
    return jsonify(clients)

@app.route("/add-client", methods=["POST"])
def add_client():
    """Add a new client to the database"""
    data = request.json
    name = data.get("name")
    age = data.get("age")
    height = data.get("height")
    weight = data.get("weight")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO clients(name,age,height,weight) VALUES (?,?,?,?)",
        (name, age, height, weight)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Client added successfully"})

# ---------- BMI CALCULATOR ----------

@app.route("/bmi")
def bmi():
    """Calculate BMI based on height (cm) and weight (kg)"""
    try:
        height = float(request.args.get("height"))
        weight = float(request.args.get("weight"))
        h = height / 100
        bmi_value = weight / (h * h)
        return jsonify({"BMI": round(bmi_value, 2)})
    except (TypeError, ValueError):
        return jsonify({"error": "Please provide valid height and weight"}), 400

# ---------- RUN APP ----------

if __name__ == "__main__":
    app.run(debug=True)
