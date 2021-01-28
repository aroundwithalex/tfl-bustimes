from flask import render_template, jsonify
from .fetch import fetch_data, data_for_display
from app import app


@app.route("/")
def index():
    data = fetch_data()
    display_data = data_for_display(data)
    return render_template("index.html", data=display_data)


@app.route("/raw_json.html")
def raw_data():
    data = fetch_data()
    return jsonify(data)
