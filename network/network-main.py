import time
from subscriber import Subscriber

if __name__ == "__main__":
    broker = "test.mosquitto.org"
    port = 1883
    keepalive = 10
    subscriber = Subscriber(broker, port, keepalive)
    try:
        subscriber.connect()
    except Exception as ex:
        print("Connection could not be established")
        print("reason : ", ex)
    try:
        subscriber.listen()
    except KeyboardInterrupt:
        print("Disconnecting..")
        subscriber.disconnect()
        time.sleep(2)
        print("Disconnected successfully")
    except RuntimeError:
        print("Could not connect to Raspberry, check your connection")
