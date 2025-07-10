# 1. federated_learning_server.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def receive_model():
    weights = request.json.get("weights")
    if weights:
        print("Received model weights update.")
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
