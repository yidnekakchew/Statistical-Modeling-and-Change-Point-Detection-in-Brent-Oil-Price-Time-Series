# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Sample data for Brent oil prices
DATA = [
    {"date": "2023-01-01", "price": 80, "event": "Event A"},
    {"date": "2023-01-02", "price": 82, "event": "Event B"},
    {"date": "2023-01-03", "price": 78, "event": "Event C"},
    # More data points can be added here
]

@app.route('/api/prices', methods=['GET'])
def get_prices():
    return jsonify(DATA)

if __name__ == '__main__':
    app.run(debug=True)
