import time

from publisher import Publisher

landmark_data = {
                "hand": "right",
                "landmarks": [[0.5, 0.5, 0.0] for _ in range(21)]  # Dummy data
            }
if __name__ == "__main__":
    com_rate = 1
    broker = "test.mosquitto.org"
    port = 1883
    publisher = Publisher(com_rate=com_rate, broker=broker, port=port)
    publisher.connect()
    try:
        publisher.publish(landmark_data)
    except KeyboardInterrupt:
        print("Shutting down..")
        publisher.disconnect()
        time.sleep(2)
        print("Shut down successfully")