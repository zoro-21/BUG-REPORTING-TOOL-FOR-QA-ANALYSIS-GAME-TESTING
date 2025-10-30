# app.py - Flask Bug Reporting Tool
from flask import Flask, g, render_template, request, redirect, url_for, jsonify
import sqlite3
import os

DB = "bugs.sqlite"
app = Flask(__name__, static_folder='static', template_folder='templates')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cur = db.execute("SELECT * FROM bugs ORDER BY created_at DESC")
    bugs = cur.fetchall()
    return render_template('bugs.html', bugs=bugs)

@app.route('/add', methods=['POST'])
def add_bug():
    data = request.form
    db = get_db()
    db.execute("INSERT INTO bugs (title, description, severity, status, created_at) VALUES (?,?,?,?,datetime('now'))",
               (data.get('title'), data.get('description'), data.get('severity'), data.get('status')))
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:bug_id>', methods=['POST'])
def delete_bug(bug_id):
    db = get_db()
    db.execute("DELETE FROM bugs WHERE id=?", (bug_id,))
    db.commit()
    return redirect(url_for('index'))

@app.route('/api/bugs')
def api_bugs():
    db = get_db()
    rows = db.execute("SELECT * FROM bugs ORDER BY created_at DESC").fetchall()
    return jsonify([dict(r) for r in rows])

if __name__ == '__main__':
    if not os.path.exists(DB):
        print("Database not found, run init_db.py to create it.")
    app.run(debug=True)
