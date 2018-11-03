"""Temporary module for developing mqtt comm handler"""

from multiprocessing import Queue
import comm_handlers
import logging_setup

logger = logging_setup.aux_logger()


queue = Queue(10)
queue.put(("address", "data"))

comm_handlers.mqtt(queue, comm_handlers.MQTT_PORT)
