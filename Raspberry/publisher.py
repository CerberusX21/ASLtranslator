import paho.mqtt.client as mqtt
import json
import time
class Publisher:
    def __init__(self,com_rate,broker, port):
        self.client = mqtt.Client()
        self.com_rate = com_rate
        self.broker = broker
        self.port = port

    def connect(self):
        self.client.connect(host=self.broker, port=self.port)

    def publish(self, message):
        topic = "ASL"
        while True:
            self.client.publish(topic, json.dumps(message), 0)
            print("Published hand landmarks")
            time.sleep(self.com_rate)

    def disconnect(self):
        self.client.disconnect()