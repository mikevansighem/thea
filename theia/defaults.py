"""Default values shared between modules or used by __main__.py.

Other default values can be defined within the module where they are
being used."""

# MQTT
MQTT_PORT = 1185
MQTT_ADRESS = "127.0.0.1"
MQTT_REQUEST_CONFIG_TOPIC = "+/request_config"
MQTT_SUPPLY_CONFIG_TOPIC = "+/supply_config"
MQTT_STATUS_TOPIC = "+/status"
