"""Top-level package for Thea

This module import attributes of Thea. Everything made explicitly
available via `__all__` can be considered as part of the Thea API.
"""

# flake8: noqa E402

# Define metadata before logger setup so it can be included in logs.
# __version__ = "0.0.1"

# Setup logger before anything else. Necessary because imported sub-modules
# import logger from the package level.
from . import logging_setup

logger = logging_setup.main_logger()

# Now the logger is setup import the public objects
from .thea_world import TheaWorld
from .cli import cli_app
from . import exceptions
from .mqtt_hardware_module import cli_mqtt_hw_module, MQTTHardwareModule

# Define public API
__all__ = [
    "cli_app",  # cli-app
    "cli_mqtt_hw_module"  # cli hardware module
    "exceptions",  # Thea specific exceptions
    "TheaWorld",  # Thea base class exposing all functionalities
    "MQTTHardwareModule",  # Mqtt moule base class exposing all functionalities
]
