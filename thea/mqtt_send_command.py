import paho.mqtt.client as mqtt
import pickle

broker_address = "127.0.0.1"
client = mqtt.Client("Command")
client.connect(broker_address, 1185)
client.publish("module_44831927329495/topic3", pickle.dumps(True))
