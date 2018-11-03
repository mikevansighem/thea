"""MQTT hardware module that can be started from the cli"""

import paho.mqtt.client as mqtt
import argparse
import pickle
import uuid
import arrow
import logging
import logging_setup
from exceptions import IgnoreSaved
from comm_handlers.mqtt_constants import (
    MQTT_ADRESS,
    MQTT_PORT,
    MQTT_REQUEST_CONFIG_TOPIC,
    MQTT_SUPPLY_CONFIG_TOPIC,
    MQTT_STATUS_TOPIC,
)

SAVED_STATE_FILE_NAME = "state_MQTT_module.pickle"
AUTOSAVE_INTERVAL = 60 * 5
STATUS_POST_INTERVAL = 60

# Setup logger
logger = logging_setup.aux_logger()


def new_config_callback(client, userdata, message):

    received_config = pickle.loads(message.payload)
    logger.info(f"Received new configuration from controller.")
    logger.debug(f"Received configuration: '{received_config}'.")
    client.received_config = received_config


class MQTTHardwareModule:
    def __init__(self, hardware_type, ignore_config=False):

        # Set fixed hardware type and identifier
        self.hardware_type = hardware_type
        logger.debug(f'Hardware type is set to "{self.hardware_type}"')
        self.unique_identifier = f"module_{uuid.getnode()}"
        logger.debug(f'Unique identifier is set to "{self.unique_identifier}"')

        # Create MQTT client
        self.client = mqtt.Client(self.unique_identifier)

        # Set the will to revert status to False upon disconnect
        self.client.will_set(
            topic=MQTT_STATUS_TOPIC.replace("+", self.unique_identifier),
            payload=pickle.dumps(False),
            qos=2,
            retain=True,
        )

        # Connect
        while True:

            try:
                self.client.connect(MQTT_ADRESS, MQTT_PORT)
                break
            except ConnectionRefusedError:
                logger.warning(
                    f"Failed to connect with MQTT broker at {MQTT_ADRESS}:{MQTT_PORT}."
                )

        logger.info(f"Connected with MQTT broker at {MQTT_ADRESS}:{MQTT_PORT}.")

        # Set status to not ready
        self.publish(MQTT_STATUS_TOPIC, False)

        # Hardware module with configuration
        try:

            # Hack to ignore configuration
            if ignore_config:
                raise IgnoreSaved("Ignoring configuration.")

            # Check if a previous config is present
            self.config = self.load_config()

            # Check if the identifier matches
            if self.config["unique_identifier"] != self.unique_identifier:
                raise Exception("Unique_identifier in configuration does not match.")

        except (IgnoreSaved, FileNotFoundError):

            # Request a new config
            logger.warning("No valid configuration found.")
            self.config = self.request_config()

        finally:

            logger.info("Completed retrieval of a configuration.")

        # Setup is completed run module
        self.run()

    def load_config(self) -> dict:
        """Loads configuration from file"""

        config = pickle.load(open(SAVED_STATE_FILE_NAME, "rb"))
        logger.info(f'Loaded configuration from "{SAVED_STATE_FILE_NAME}"')
        return config

    def request_config(self):

        # Ensure there is no old config on the client object
        self.client.received_config = None
        # Add a callback to handle a new configuration
        self.client.message_callback_add(
            MQTT_SUPPLY_CONFIG_TOPIC.replace("+", self.unique_identifier),
            new_config_callback,
        )
        # Subscribe to receive new configuration
        self.client.subscribe(
            MQTT_SUPPLY_CONFIG_TOPIC.replace("+", self.unique_identifier)
        )
        # Request new configuration with the current utc time
        self.publish(MQTT_REQUEST_CONFIG_TOPIC, arrow.utcnow())
        logger.info("Requested new configuration.")

        while self.client.received_config is None:
            self.client.loop()
            logger.debug("Waiting for new configuration.")

        return self.client.received_config

    def publish(self, topic_template, data):
        """Publish to a topic preceded by the module id"""

        topic = topic_template.replace("+", self.unique_identifier)
        data = pickle.dumps(data)
        self.client.publish(topic, data)

    def renew_status(self):
        """Send alive status"""

        try:
            if (arrow.utcnow() - self.last_status_post).seconds > STATUS_POST_INTERVAL:
                self.publish(MQTT_STATUS_TOPIC, True)
                self.last_status_post = arrow.utcnow()
                logger.debug("Renewed status.")

        except AttributeError:
            self.publish(MQTT_STATUS_TOPIC, True)
            self.last_status_post = arrow.utcnow()
            logger.debug("Renewed status.")

    def auto_save(self):
        """auto save configuration"""

        try:
            if (arrow.utcnow() - self.last_save).seconds > AUTOSAVE_INTERVAL:
                self.save()
        except AttributeError:
            self.save()

    def save(self):
        """Save state to file"""

        pickle.dump(self.config, open(SAVED_STATE_FILE_NAME, "wb"))
        self.last_save = arrow.utcnow()
        logger.debug(f'Saved configuration to "{SAVED_STATE_FILE_NAME}".')

    def run(self):

        logger.info("Starting loop.")

        while True:

            self.renew_status()
            self.auto_save()

            # Process messages
            self.client.loop()


def main():
    """Handles initial argument to start the hardware module."""

    parser = argparse.ArgumentParser(
        description="Starts a (simulated) MQTT hardware module from the CLI."
    )
    parser.add_argument(
        "-t", "--type", help="Hardware type.", default="placeholder_hardware_type"
    )
    parser.add_argument(
        "-v", "--verbose", help="Verbose printing.", action="store_true"
    )
    parser.add_argument(
        "-i",
        "--ignore_config",
        help="Ignore previous configuration.",
        action="store_true",
    )
    args = parser.parse_args()

    # Set verbosity level of logger
    if args.verbose is True:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Initialize and run
    MQTTHardwareModule(args.type, args.ignore_config).run()


if __name__ == "__main__":
    main()
