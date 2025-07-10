import socket
from config import config


def listen_for_alerts():
    """
    Listens for V2X broadcast messages and prints them when received.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", config.V2X_PORT))

    print("Listening for V2X alerts...")
    while True:
        message, addr = sock.recvfrom(1024)
        print(f"Received V2X alert from {addr}: {message.decode()}")


if __name__ == "__main__":
    listen_for_alerts()
