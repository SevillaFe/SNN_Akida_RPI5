# 2. federated_learning_client.py

import requests
import numpy as np
import json

# Replace with the actual IP address or 'localhost' if server is local
SERVER_IP = "localhost"
UPLOAD_URL = f"http://{SERVER_IP}:5000/upload"

# Dummy model to simulate Akida weight extraction
class DummyAkidaModel:
    def get_weights(self):
        # Return dummy weights for demonstration
        return np.random.rand(10)

# Instantiate and extract weights
model_akida = DummyAkidaModel()
model_weights = model_akida.get_weights()

# Convert weights to list for JSON serialization
weights_data = {"weights": model_weights.tolist()}

# Upload to federated server
try:
    response = requests.post(UPLOAD_URL, json=weights_data)
    if response.status_code == 200:
        print("Model weights uploaded successfully.")
    else:
        print(f"Error uploading model weights: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Connection failed:", e)
