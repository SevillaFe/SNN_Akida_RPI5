# scripts/mqtt_publisher.py

import paho.mqtt.client as mqtt
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from config import config

# Optional: Use real Akida inference if available
try:
    from akida import Model, devices
    device = devices()[0]
    device.soc.power_measurement_enabled = True

    # Load Akida model
    model_akida = Model("sample_data/model.fbz")  # Replace with actual model path
    model_akida.map(device)

    # Prepare input
    x_test = np.load("sample_data/dummy_input.npy")
    sample_image = x_test[0].reshape(1, 28, 28, 1)

    # Run Akida inference
    outputs = model_akida.forward(sample_image)
    stats = model_akida.statistics
    power = stats.power
    latency = stats.time

except ImportError:
    print("Akida SDK not found. Running with dummy inference.")
    x_test = np.load("sample_data/dummy_input.npy")
    sample_image = x_test[0].reshape(1, 28, 28, 1)
    outputs = np.random.rand(1, 10)
    power = None
    latency = None

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

if power is not None and latency is not None:
    inference_result["power_mW"] = round(power, 2)
    inference_result["latency_ms"] = round(latency, 2)

client.publish(config.TOPIC, json.dumps(inference_result))
print("Inference result sent:", inference_result)

# Visualize
plt.imshow(sample_image.squeeze(), cmap=cm.Greys_r)
plt.title(f"Class: {predicted_class} | Confidence: {confidence:.2f}")
plt.show()

