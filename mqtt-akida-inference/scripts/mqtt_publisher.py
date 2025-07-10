# scripts/mqtt_publisher.py

import paho.mqtt.client as mqtt
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from config import config

# Dummy model output
x_test = np.load("sample_data/dummy_input.npy")  # Replace with real dataset
sample_image = x_test[0].reshape(1, 28, 28, 1)

# Simulate Akida inference
outputs = np.random.rand(1, 10)
predicted_class = np.argmax(outputs)
confidence = np.max(outputs)

# MQTT client
client = mqtt.Client()
client.connect(config.BROKER_IP, config.MQTT_PORT, 60)

inference_result = {
    "device": config.DEVICE_ID,
    "classification": int(predicted_class),
    "confidence": float(confidence)
}

client.publish(config.TOPIC, json.dumps(inference_result))
print("Inference result sent:", inference_result)

# Visualize
plt.imshow(sample_image.squeeze(), cmap=cm.Greys_r)
plt.title(f"Class: {predicted_class} | Confidence: {confidence:.2f}")
plt.show()
