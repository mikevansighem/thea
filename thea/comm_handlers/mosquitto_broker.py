"""Module for starting and stopping the Mosquito mqtt broker"""

# TODO: re-factor so with open can be used on it

import logging
import subprocess
import time
import atexit
from ..exceptions import MQTTBrokerError, MQTTBrokerPortNotAvailible

START_BROKER_TIMEOUT = 5  # seconds
MOSQUITTO_PORT_IN_USE = "Error: Only one usage of each socket address (protocol/network address/port) is normally permitted."
MOSQUITTO_STARTED = "Opening ipv4 listen socket on port"

logger = logging.getLogger(__name__)


def start_mqtt_broker(port):

    # Start the broker process
    broker_process = subprocess.Popen(
        ["mosquitto", "-p", str(port), "-v"], stderr=subprocess.PIPE, bufsize=1
    )

    # Ensure the process is killed at exit
    atexit.register(stop_mqtt_broker, broker_process)
    # TODO: check if this is for the current process or the whole program

    # Wrap in try/except to ensure the process gets killed if an exception occurs.
    try:

        # Timeout if the broker does not respond with a success message
        start_time = time.time()
        while (time.time() - start_time) < START_BROKER_TIMEOUT:

            # Get latest message
            error_message = read_broker_stderr(broker_process)

            # Look for port error
            if MOSQUITTO_PORT_IN_USE in error_message:
                raise MQTTBrokerPortNotAvailible(
                    f"Could not start MQTT broker, port {port} already in use."
                )

            elif MOSQUITTO_STARTED in error_message:
                logger.info(f"Started MQTT broker at port {port}.")
                return broker_process

            # Catch all other errors and raise exception
            elif "Error" in error_message:
                raise MQTTBrokerError(
                    f'MQTT broker exited with message: "{error_message}"'
                )

        raise MQTTBrokerError(
            f"Starting MQTT broker timed-out after {START_BROKER_TIMEOUT} seconds."
        )

    except Exception as some_exception:
        # Kill broker if an exception is not handled
        stop_mqtt_broker(broker_process)

        # Re-raise Exception
        raise some_exception from None


def read_broker_stderr(broker_process):

    line = broker_process.stderr.readline()
    line = line.replace(b"\n", b"").replace(b"\r", b"")

    if line != b"":

        line = line.decode()
        logger.debug(f'Message outputted by MQTT broker: "{line}"')
        return line


def stop_mqtt_broker(broker_process):
    """Kills broker process."""

    broker_process.terminate()
    broker_process.kill()
    logger.info("Killed broker process.")


def broker_status(broker_process):
    """Returns a `bool` indicating if the broker process is running."""

    if broker_process.poll() is None:
        return True
    else:
        return False
