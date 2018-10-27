"""Default values shared between modules or used by __main__.py.

Other default values can be defined within the module where they are
being used."""

import arrow
from string import Template
from env_updaters import StackedLinearModel


# Name for creating a item without a specific name
BASEITEM_NAME_TEMPLATE = Template("$type_$number")

# Enviroment variables
ENV_VARIABLES = {}
ENV_VARIABLES["datetime"] = arrow.utcnow()

# Enviroment settings
ENV_SETTINGS = {}
ENV_SETTINGS["time_factor"] = 10000
ENV_SETTINGS["country"] = "netherlands"
ENV_SETTINGS["latitude"] = 52.3
ENV_SETTINGS["longitude"] = 4.8

# Shop model
shops_model = StackedLinearModel("day")
shops_model.add_point(arrow.get("07:00", "HH:mm"), 0)
shops_model.add_point(arrow.get("10:00", "HH:mm"), 0.9)
shops_model.add_point(arrow.get("17:00", "HH:mm"), 0.9)
shops_model.add_point(arrow.get("22:00", "HH:mm"), 0)
ENV_SETTINGS["shops_model"] = shops_model

# MQTT
MQTT_PORT = 1185
MQTT_NEW_HARDWARE_TOPIC = '+/request_config'
MQTT_HARDWARE_CONFIG_TOPIC = '+/new_config'
MQTT_READY_FOR_OPERATION = '+/ready'
