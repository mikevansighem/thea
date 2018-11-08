"""Temporary module for developing mqtt comm handler"""

from multiprocessing import Queue
from . import comm_handlers

queue = Queue(10)
queue.put(("address", "data"))

comm_handlers.mqtt(queue, comm_handlers.MQTT_PORT)
