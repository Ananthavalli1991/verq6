# api/index.py
import csv
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all domains

# Load CSV into memory
marks_data = {}
with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks_data[row["name"]] = int(row["marks"])

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    result = [marks_data.get(name, None) for name in names]
    return jsonify({"marks": result})
