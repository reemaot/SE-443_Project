import paho.mqtt.client as paho
import json

#broker = "10.54.27.114"
#broker = "localhost"
#broker = "test.mosquitto.org"
broker = "broker.emqx.io"
#broker = "broker.hivemq.com"

def check_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True

def on_message(client, userdata, msg):

    mymessage = msg.payload

    if check_json(mymessage):
        new_bytes_start = json.loads(mymessage.decode("utf-8"))
        print(new_bytes_start['OneString'])

    else:
        print("Not a valid JSON")

client = paho.Client()
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe("reema-191244")

client.loop_forever()