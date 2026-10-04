"""Intentionally flawed, synthetic, in-memory course example. Do not deploy."""
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/lessons")
def lessons():
    topic = request.args.get("topic", "Git")
    db = sqlite3.connect(":memory:")
    try:
        db.execute("CREATE TABLE lessons (title TEXT, topic TEXT)")
        db.executemany("INSERT INTO lessons VALUES (?, ?)", [
            ("First commit", "Git"), ("First workflow", "Actions"),
        ])
        rows = db.execute("SELECT title FROM lessons WHERE topic = ?", (topic,)).fetchall()
        return jsonify([row[0] for row in rows])
    finally:
        db.close()
