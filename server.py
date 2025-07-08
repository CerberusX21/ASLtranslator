import socket
import json
from model import classify_sign  # dummy to start

UDP_IP = "0.0.0.0"
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, _ = sock.recvfrom(8192)
    landmarks = json.loads(data)
    result = classify_sign(landmarks)
    print("🖐️ Detected:", result)
