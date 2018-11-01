import paho.mqtt.client as mqtt
import argparse
import logging
from defaults import MQTT_PORT, MQTT_NEW_HARDWARE_TOPIC, MQTT_HARDWARE_CONFIG_TOPIC
from random import randint

HARDWARE_CONFIG_VIRTUAL = "virtual"
# Create random client name
INITIAL_CLIENT_NAME = f"theia_hardwaremodule_{randint(0, 100000000):08d}"
MQTT_ADRESS = "127.0.0.1"


class MQTTHardwareModule:
    def __init__(self, mqtt_adress, mqtt_port, hardware_config):
        """Initialize for specific hardware configuration."""

        # TODO add loading saves state
        # If there is a saves state use that and run
        # If not request one

        self.mqtt_port = mqtt_port
        self.adress = mqtt_adress
        self.hardware_config = hardware_config

    def run(self):
        """Run the endless main loop on the selected hardware."""

        while True:

            # Do hardware specific tasks
            if self.hardware_config == HARDWARE_CONFIG_VIRTUAL:
                self._run_virtal()
            else:
                raise NotImplementedError(
                    f"{self.hardware_config} is not a supported hardware configuration."
                )

    def _run_virtual(self):
        """actions specific for virtual hardware."""
        pass

    def _setup_as_new():

        self.mqtt_client = mqtt.Client(INITIAL_CLIENT_NAME)

        # Add as attribute for logging
        self.mqtt_client.port = mqtt_port
        self.mqtt_client.adress = mqtt_adress

        mqtt_client.connect("127.0.0.1", mqtt_port)

        # Subscribe to the configuration topic
        mqtt_client.subscribe(
            MQTT_HARDWARE_CONFIG_TOPIC.replace("+", INITIAL_CLIENT_NAME)
        )

        # Wait for the new configuration

        # Initialize configuration

        # Publish to ready topic

        # Return to normal loop


def main():

    parser = argparse.ArgumentParser(
        description="Starts a (simulated) MQTT hardware module from the CLI."
    )
    parser.add_argument(
        "-a", "--adress", help="MQTT broker adress.", default=MQTT_ADRESS
    )
    parser.add_argument("-p", "--port", help="MQTT broker port.", default=MQTT_PORT)
    parser.add_argument(
        "-c",
        "--config",
        help="Hardware configuration.",
        default=HARDWARE_CONFIG_VIRTUAL,
    )
    parser.add_argument(
        "-v", "--verbose", help="Verbose printing.", action="store_true"
    )
    args = parser.parse_args()

    # Set verbosity level of logger
    if args["verbose"] is True:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Initialize and run
    MQTTHardwareModule(args["adress"], args["port"], args["config"]).run()


if __name__ == "__main__":
    main()
