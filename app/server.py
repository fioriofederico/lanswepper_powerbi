from flask import Flask, jsonify
import pandas as pd
from .config import CSV_PATH

app = Flask(__name__)

@app.route("/api/assets")
def get_assets():
    df = pd.read_csv(CSV_PATH)
    return jsonify(df.to_dict(orient="records"))

def run_server():
    app.run(port=5000)
