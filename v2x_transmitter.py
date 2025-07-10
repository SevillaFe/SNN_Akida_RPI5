import socket
from config import config


def send_v2x_alert():
    """
    Broadcasts a simulated Akida AI event (e.g., pedestrian detection)
    over the V2X communication network.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    event_message = "V2X Alert: Pedestrian detected with 95% confidence"
    sock.sendto(event_message.encode(), (config.V2X_BROADCAST_IP, config.V2X_PORT))
    print("V2X Neuromorphic AI alert sent:", event_message)


if __name__ == "__main__":
    send_v2x_alert()
