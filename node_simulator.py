# Step 2: node_simulator.py
import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "localhost"
PORT = 1883
NODE_IDS = [1, 2, 3, 4]
PUBLISH_INTERVAL_SEC = 2  # how often each node "reports in"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)
client.loop_start()  # runs network loop in background thread

def generate_fake_reading(node_id):
    return {
        "node_id": node_id,
        "distance_cm": round(random.uniform(20.0, 500.0), 1),
        "vehicle_count": random.randint(0, 12),
        "timestamp": int(time.time())
    }

print("Starting 4-node simulator. Press Ctrl+C to stop.")

try:
    while True:
        for node_id in NODE_IDS:
            reading = generate_fake_reading(node_id)
            topic = f"trapiksense/node{node_id}/telemetry"
            payload = json.dumps(reading)
            client.publish(topic, payload)
            print(f"Published to {topic}: {payload}")
        time.sleep(PUBLISH_INTERVAL_SEC)

except KeyboardInterrupt:
    print("\nStopping simulator.")
    client.loop_stop()
    client.disconnect()