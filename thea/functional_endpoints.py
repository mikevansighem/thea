import logging
from collections import namedtuple
from queue import Queue
from threading import Thread

from .mqtt_hardware_types import HARDWARE_TYPES

logger = logging.getLogger(__name__)


def handler(hardware_type, setter, endpoints, **properties):
    """Runs a setter class in a separate process."""

    # setup of setter class
    setter = setter(hardware_type=hardware_type, endpoints=endpoints, **properties)

    # Running the setter class
    queue = Queue(5)
    worker = Thread(target=setter.run, args=(queue,))
    worker.setDaemon(True)
    worker.start()

    return worker, queue


class Setter:
    """A class to control which endpoints to change when."""

    def __init__(self, hardware_type, endpoints, **unused):
        """Setup of the setter"""

        self.hardware_config = HARDWARE_TYPES[hardware_type]
        self.endpoints = endpoints

    def run(self, queue):
        while True:
            if queue.empty() is False:
                value = queue.get()
                for endpoint in self.endpoints:
                    self.hardware_config[endpoint](value)


# Setters must all be inherited from the setter class
functionalOutput = namedtuple("functionalOutput", ["setter", "default_properties"])

# Key is the name item is an instance of functionalOutput
FUNCTIONAL_OUTPUT_SETTERS = {
    "switch": functionalOutput(setter=Setter, default_properties={}),
    "blink": functionalOutput(setter=Setter, default_properties={"interval": 1}),
}

# type is a functional output type
topicConfig = namedtuple("topicConfig", ["type_", "endpoints", "properties"])

# key is the topic, item is an instance of topic configuration
CONFIGURATION_EXAMPLE = {
    "topic1": topicConfig("switch", [1, 2, 3], {}),
    "topic2": topicConfig("blink", [0, 5], {"interval": 5}),
    "topic3": topicConfig("switch", [4], {}),
}
