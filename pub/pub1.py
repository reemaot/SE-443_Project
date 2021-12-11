import paho.mqtt.client as paho
import json

#broker = "10.54.27.114"
#broker = "localhost"
broker = "broker.emqx.io"
#broker = "broker.hivemq.com"

client = paho.Client()
client.connect(broker, 1883)

# JSON string
student ={"OneString": "se-443"}

client.publish("reema-191244", payload = json.dumps(student))
