### Run the script on the RPI5 and subscribe to the MQTT topic from another machine to receive the results:

mosquitto_sub -h <BROKER_IP> -t "akida/inference" -v
