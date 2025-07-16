from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(message="Welcome to Flask Monitoring App!", timestamp=str(datetime.datetime.utcnow()))

@app.route("/health")
def health():
    return "Healthy", 200

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    return jsonify(received=data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
