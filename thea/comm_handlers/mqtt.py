"""A comm_handler is a function that handles communication to hardware

A comm handling function has the following requirements/characteristics:
- It will always be run in a separate process.
- It starts out by connecting to its targets.
- It terminates the processes if a connection could not be established.
- It processes messages from a Queue object.
- A message is a tuple of an address and data.
- First argument is the message queue
- Other arguments are passes as kwargs and should be defined in communicator_types.py


How is new hardware handled??
How to handle a failed message that has already been removed from the queue??

"""

import logging
import pickle
from random import randint
import paho.mqtt.client as paho_mqtt
from .mosquitto_broker import start_mqtt_broker, stop_mqtt_broker, broker_status

# Create random client name
MQTT_CLIENT_NAME = f"thea_mainapp_{randint(0, 100000000):08d}"

logger = logging.getLogger(__name__)


def on_connect():
    """On connect the client subscribes to the new hardware topic."""

    # TODO

    pass


def on_message():
    """Handle received message"""

    # TODO: filter for new hardware topic

    pass


def mqtt(message_queue, properties):
    """Handles the mqtt broker and forwarding messages over mqtt.
    This will be run as a subprocess. As long as it is alive we can
    assume the broker and client are both functioning."""

    mqtt_port = properties["mqtt_port"]
    logger.debug(f"MQTT comm handler received port property: '{mqtt_port}'")

    # Start the broker
    # broker_process = start_mqtt_broker(mqtt_port)

    # Create client object
    mqtt_client = paho_mqtt.Client(MQTT_CLIENT_NAME)

    # Add port as attribute for logging
    mqtt_client.port = mqtt_port

    # TODO Assign event handlers
    # mqtt_client.on_message = on_message

    mqtt_client.enable_logger(logger=logger)
    mqtt_client.connect("127.0.0.1", mqtt_port)

    # While the broker is running
    while True:  # broker_status(broker_process):

        mqtt_client.loop()

        # Get oldest item from message queue
        adress, data = message_queue.get()

        # TODO: Get topic to send the message to
        topic = adress

        # Publish pickled data
        mqtt_client.publish(topic, pickle.dumps(data))

    # Exit if the broker process stopped
    mqtt_client.disconnect()
    stop_mqtt_broker(broker_process)
