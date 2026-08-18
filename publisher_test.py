#Test 1
# publisher_test.py
import paho.mqtt.client as mqtt
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)

client.publish("test/topic", "hello from python")
time.sleep(1)  # give it a moment to send before disconnecting
client.disconnect()