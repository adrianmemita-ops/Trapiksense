# Step 2: telemetry_listener.py
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code: {reason_code}")
    client.subscribe("trapiksense/+/telemetry")  # '+' wildcard matches any node number

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()