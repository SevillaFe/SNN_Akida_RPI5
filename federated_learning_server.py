## Use Case: If multiple RPI5-Akida nodes are deployed for federated learning, updates to neuromorphic models must be synchronized between devices
### Uploading Akida Model Weights to a Federated Learning Server


import requests
import numpy as np
import json

# ---- Configuration ----

SERVER_IP = "000.000.0.000"  # Here the actual server IP
UPLOAD_URL = f"http://{SERVER_IP}:5000/upload"  # API endpoint for model updates

# ---- Extract & Convert Model Weights ----

# Get model weights from the trained Akida model
model_weights = model_akida.get_weights()  # Extract trained model weights

# Convert weights to JSON format
weights_data = {"weights": np.array(model_weights).tolist()}  # Ensure conversion to list format

# ---- Send Weights to Federated Server ----

# Send model weights to the central server using an HTTP POST request
response = requests.post(UPLOAD_URL, json=weights_data)

# Check response status
if response.status_code == 200:
    print("Model weights uploaded successfully.")
else:
    print("Error uploading model weights:", response.status_code)


### To use it first, we run a simple Flask-based server to receive model updates:

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

