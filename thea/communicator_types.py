from collections import namedtuple

from . import comm_handlers

# Values of the named tuple need to be of type: any, list of types, dict, callable
CommunicatorType = namedtuple(
    "CommunicatorType", ["comm_handler", "default_properties"]
)

# A contradictory of all ThingTypes
COMMUNICATOR_TYPES = {}
COMMUNICATOR_TYPES["mqtt"] = CommunicatorType(
    comm_handler=comm_handlers.mqtt,
    default_properties={"mqtt_port": comm_handlers.MQTT_PORT},
)
