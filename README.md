# SNN_Akida_RPI5
Eco-Efficient Deployment of Spiking Neural Networks on Low-Cost Edge Hardware

This work presents a practical and energy-aware framework for deploying Spiking Neural Networks on low-cost hardware for edge computing. We detail a reproducible pipeline that integrates neuromorphic processing with secure remote access and distributed intelligence. Using Raspberry Pi and the BrainChip Akida PCIe accelerator, we demonstrate a lightweight deployment process including model training, quantization, and conversion. Our experiments validate the eco-efficiency and networking potential of neuromorphic AI systems, providing key insights for sustainable distributed intelligence. This letter offers a blueprint for scalable and secure neuromorphic deployments across edge networks.

## 1. Hardware and Software Setup
The proposed deployment platform integrates two key hardware components: the RPI5 and the Akida board. Together, they enable a power-efficient, cost-effective N-S suitable for real-world edge AI applications.

## 2. Enabling Secure Remote Access and Distributed Neuromorphic Edge Networks
The deployment of low-power N-H in networked environments requires reliable, secure, and lightweight communication frameworks. Our system enables full remote operability of the RPI5 and Akida board via SSH, complemented by protocol layers (Message Queuing Telemetry Transport (MQTT), WebSockets, Vehicle-to-Everything (V2X)) that support real-time, event-driven intelligence across edge networks.

## 3. Training and Running Spiking Neural Networks
The training pipeline begins with building an ANN using TensorFlow 2.x, which will later be mapped to a spike-compatible format for neuromorphic inference. Because Akida board runs models using low-bitwidth integer arithmetic (4–8 bits), it is critical to align the training phase with these constraints to avoid significant post-training performance degradation.

## 4. Use case validation: Networked neuromorphic AI for distributed intelligence
### 4.1  Use Case: If multiple RPI5 nodes or remote clients need to receive the classification results in real-time, MQTT can be used to broadcast inference outputs


### 4.2 Use Case: If the Akida accelerator is deployed in an autonomous driving system, V2X communication allows other vehicles or infrastructure to receive AI alerts based on neuromorphic-based vision

This Use Cases simulates a lightweight V2X (Vehicle-to-Everything) communication system using Python. It demonstrates how neuromorphic AI event results, such as pedestrian detection, can be broadcast over a network and received by nearby infrastructure or vehicles.

## Folder Structure
```
.
├── config
│   └── config.py              # V2X settings
├── transmitter
│   └── v2x_transmitter.py     # Simulated Akida alert broadcaster
├── receiver
│   └── v2x_receiver.py        # Listens for incoming V2X alerts
└── README.md
```

## Use Case
If the Akida accelerator is deployed in an autonomous driving system, this setup allows:
- Broadcasting high-confidence AI alerts (e.g., "pedestrian detected")
- Receiving alerts on nearby systems for real-time awareness

## Usage

### 1. Start the V2X Receiver (on vehicle or infrastructure node)
```bash
python3 receiver/v2x_receiver.py
```

### 2. Run the Alert Transmitter (on an RPI5 + Akida node)
```bash
python3 transmitter/v2x_transmitter.py
```

## Notes
- Ensure that devices are on the same LAN or wireless network
- UDP broadcast mode is used for simplicity
- This is a prototype for real-time event-based message sharing between intelligent nodes

## License
MIT License


### 4.3 Use Case: If multiple RPI5-Akida nodes are deployed for federated learning, updates to neuromorphic models must be synchronized between devices

# Federated Learning Setup with Akida on Raspberry Pi 5

This repository demonstrates a lightweight Federated Learning (FL) setup using neuromorphic AI models deployed on BrainChip Akida PCIe accelerators paired with Raspberry Pi 5 devices. It provides scripts for a centralized Flask server to receive model weight updates and a client script to upload Akida model weights via HTTP.

## Overview

Neuromorphic models trained on individual RPI5-Akida nodes can contribute updates to a shared model hosted on a central server. This setup simulates a federated learning architecture for edge AI applications that require privacy, low latency, and energy efficiency.

## Repository Structure

```
├── federated_learning_server.py       # Flask server to receive model weights
├── federated_learning_client.py       # Client script to upload Akida model weights
├── model_utils.py                     # (Optional) Placeholder for weight handling utilities
├── model_training.py                  # (Optional) Placeholder for training-related code
└── README.md
```

## Requirements

- Python 3.7+
- Flask
- NumPy
- Requests
- Akida Python SDK (required on client device)

Install the dependencies using:

```bash
pip install flask numpy requests
```

## Getting Started

### 1. Launch the Federated Learning Server

On a device intended to act as the central server:

```bash
python3 federated_learning_server.py
```

The server will listen for HTTP POST requests on port `5000` and respond to updates sent to the `/upload` endpoint.

### 2. Configure and Run the Client

On each RPI5-Akida node:

- Ensure the Akida model has been trained.
- Replace the `SERVER_IP` variable inside `federated_learning_client.py` with the IP address of the server.
- Run the script:

```bash
python3 federated_learning_client.py
```

This will extract the weights from the Akida model and transmit them to the server in JSON format.

## Example Response

After a successful POST:

```
Model weights uploaded successfully.
```

If an error occurs (e.g., connection refused or malformed weights), you will see an appropriate status message.

## Security Considerations

This is a prototype-level setup for research. For real-world deployment:
- Use HTTPS instead of HTTP.
- Authenticate clients using tokens or API keys.
- Validate the format and shape of model weights before acceptance.

## Acknowledgements

This implementation is part of a broader effort to demonstrate low-cost, energy-efficient neuromorphic AI for distributed and networked edge environments, particularly leveraging the BrainChip Akida PCIe board and Raspberry Pi 5 hardware.
