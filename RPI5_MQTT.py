## Use Case: If multiple RPI5 nodes or remote clients need to receive the classification results in real-time, MQTT can be used to broadcast inference outputs.

import paho.mqtt.client as mqtt
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# ---- Configuration ----

# Define MQTT broker details
BROKER_IP = "000.000.0.000"  # Replace with the actual IP of the MQTT broker
TOPIC = "akida/inference"  # Topic where inference results will be published

# Initialize and connect the MQTT client
client = mqtt.Client()
client.connect(BROKER_IP, 1883, 60)  # Port 1883 is the default MQTT port

# ---- Perform Inference ----

# Select a sample image from the test dataset
sample_image = x_test[0].reshape(1, 28, 28, 1)  # Reshape for model compatibility

# Perform inference with the Akida model
outputs = model_akida.predict(sample_image)

# Extract the predicted class and confidence score
predicted_class = np.argmax(outputs)  # Class with highest probability
confidence = np.max(outputs)  # Confidence score for the predicted class

# ---- Publish Inference Result ----

# Format the classification result as a JSON object
inference_result = {
    "device": "RPI5-Akida",  # Identifier for the neuromorphic AI device
    "classification": int(predicted_class),  # Predicted class (integer)
    "confidence": float(confidence)  # Confidence score (float)
}

# Publish the inference result to the MQTT broker
client.publish(TOPIC, json.dumps(inference_result))
print("Inference result sent:", inference_result)

# ---- Visualization ----

# Display the test image along with classification results
plt.imshow(sample_image.squeeze(), cmap=cm.Greys_r)
plt.title(f"Class: {predicted_class} | Confidence: {confidence:.2f}")
plt.show()
