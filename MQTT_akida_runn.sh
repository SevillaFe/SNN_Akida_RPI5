###  MQTT Broker on RPI5 to use it previously to RPI5_MQTT.py

sudo apt update
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
