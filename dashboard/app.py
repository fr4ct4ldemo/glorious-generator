from flask import Flask, render_template, jsonify
from flask_cors import CORS
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'database.db')

def get_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    db = get_db()
    servers = db.execute(
        "SELECT COUNT(DISTINCT guild_id) FROM accounts"
    ).fetchone()[0] or 0
    users = db.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0] or 0
    generated = db.execute(
        "SELECT SUM(amount_genned) + SUM(prem_amount_genned) FROM users"
    ).fetchone()[0] or 0
    db.close()
    return jsonify({
        'servers': servers,
        'users': users,
        'generated': generated
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)