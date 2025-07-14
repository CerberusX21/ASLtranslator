import json
import time

import paho.mqtt.client as mqtt
timeout = 10
global last_time
last_time = time.time()

def _on_connect(client, userdata, flags, rc):
    topic = "ASL"
    print("Connected to broker")
    client.subscribe(topic)

def _on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    last_time = time.time()
    print("Received landmarks:", data)
    return last_time

class Subscriber:
    def __init__(self, host, port, keepalive):
        self.host = host
        self.port = port
        self.keepalive = keepalive
        self.client = mqtt.Client()
        self.client.on_connect = _on_connect
        self.client.on_message = _on_message

    def connect(self):
        self.client.connect(self.host, self.port, self.keepalive)

    def listen(self):
        self.client.loop_forever()

    def disconnect(self):
        self.client.disconnect()

