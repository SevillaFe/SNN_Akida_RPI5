# scripts/mqtt_subscriber.py

import paho.mqtt.client as mqtt
from config import config

def on_message(client, userdata, message):
    print(f"Received on {message.topic}: {message.payload.decode()}")

client = mqtt.Client()
client.connect(config.BROKER_IP, config.MQTT_PORT, 60)
client.subscribe(config.TOPIC)
client.on_message = on_message

print(f"Subscribed to {config.TOPIC}, waiting for messages...")
client.loop_forever()
