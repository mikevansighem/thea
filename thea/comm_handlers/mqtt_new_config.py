"""Temporary file for generating a configuration for a hardware module."""

import paho.mqtt.client as mqtt
import uuid
import pickle
import time
from mqtt_constants import (
    MQTT_ADRESS,
    MQTT_PORT,
    MQTT_REQUEST_CONFIG_TOPIC,
    MQTT_SUPPLY_CONFIG_TOPIC,
)

##############################################################################

from collections import namedtuple

# type is a functional output type
topicConfig = namedtuple("topicConfig", ["type_", "endpoints", "properties"])

# key is the topic, item is an instance of topic configuration
CONFIGURATION_EXAMPLE = {
    "topic1": topicConfig("switch", [1, 2, 3], {}),
    "topic2": topicConfig("blink", [0, 5], {"interval": 5}),
    "topic3": topicConfig("switch", [4], {}),
}

#############################################################################


def supply_config_callback(client, userdata, message):
    """Handles a new config request"""

    module_identifier = message.topic.split("/")[0]
    print(f"Received new configuration request from {module_identifier}.")

    # Example module configuration
    new_module_configuration = CONFIGURATION_EXAMPLE

    # Publish new configuration
    client.publish(
        MQTT_SUPPLY_CONFIG_TOPIC.replace("+", module_identifier),
        pickle.dumps(new_module_configuration),
    )


def on_log_callback(client, userdata, level, buf):
    print("log: ", buf)


# Create unique identifier
unique_identifier = f"controller_{uuid.getnode()}"
print(f'Unique identifier is set to "{unique_identifier}"')

# Create MQTT client
client = mqtt.Client(unique_identifier)
client.message_callback_add(MQTT_REQUEST_CONFIG_TOPIC, supply_config_callback)

# Connect
client.connect(MQTT_ADRESS, MQTT_PORT)
# Subscribe to new config request topic
client.subscribe(MQTT_REQUEST_CONFIG_TOPIC)

client.on_log = on_log_callback
# client.enable_logger(logger=None)

# Run the loop
client.loop_start()
time.sleep(10000)
client.loop_stop()
