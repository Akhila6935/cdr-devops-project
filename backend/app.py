from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)

@app.route('/cdr')
def get_cdr():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cdr_records")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/analytics')
def analytics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(cost) FROM cdr_records")
    total_cost = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(duration) FROM cdr_records")
    avg_duration = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total_cost": total_cost,
        "avg_duration": avg_duration
    })

app.run(host="0.0.0.0", port=5000)