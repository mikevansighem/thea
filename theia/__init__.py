"""Top-level package for Theia

This module import attributes of Theia. Everything made explicitly
available via `__all__` can be considered as part of the Theia API.
"""

# flake8: noqa E402

# Define metadata before logger setup so it can be included in logs.
__author__ = "Mike van Sighem"
__email__ = "mikevansighem@gmail.com"
__version__ = "0.0.1"
__license__ = "LGPL"
__status__ = "Development"
__copyright__ = "Copyright 2018, Mike van Sighem"
__maintainer__ = "Mike van Sighem"
__credits__ = ["Mike van Sighem"]

# Setup logger before anything else. Necessary because imported sub-modules
# import logger from the package level.
from . import logging_setup

logger = logging_setup.main_logger()

# Now the logger is setup import the public objects
from .theia_world import TheiaWorld
from .cli import cli_app
from . import exceptions
from .mqtt_hardware_module import cli_mqtt_hw_module, MQTTHardwareModule

# Define public API
__all__ = [
    "cli_app",  # cli-app
    "cli_mqtt_hw_module"  # cli hardware module
    "exceptions",  # Theia specific exceptions
    "TheiaWorld",  # Theia base class exposing all functionalities
    "MQTTHardwareModule",  # Mqtt moule base class exposing all functionalities
]
