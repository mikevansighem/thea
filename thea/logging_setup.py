"""Functions to setup loggers."""

import os
import sys
import socket
import platform
import logging
import arrow
from logging.config import fileConfig

# Make log config relative to module
LOGGING_CONFIG_LOCATION = "logging.ini"
LOGS_DIRECTORY = "logs"


def log_exception(exctype, value, tb):
    """Catches exceptions in the logs"""

    logging.error("Uncaught exception:", exc_info=(exctype, value, tb))


def main_logger():
    """Sets-up main logger from configuration file."""

    log_name = f"thea_log_{arrow.utcnow().format('YYYYMMDD_HHmm')}"

    try:
        logs_dir = os.path.join(os.path.dirname(__file__), LOGS_DIRECTORY)

        # Create logs directory
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Setup log directory relative to this module
        log_file = log_name + ".log"
        logging.log_location = os.path.join(logs_dir, log_file)
        logger = fileConfig(
            os.path.join(os.path.dirname(__file__), LOGGING_CONFIG_LOCATION)
        )

    except KeyError:
        raise FileNotFoundError(f"Could not find {LOGGING_CONFIG_LOCATION}.")

    else:
        logger = logging.getLogger(__name__)

    # Set logging level for all other then Thea to warning
    for key in logging.Logger.manager.loggerDict:
        if "thea" not in key:
            logging.getLogger(key).setLevel(logging.WARNING)

    # Catch exceptions and warnings in log
    sys.excepthook = log_exception
    logging.captureWarnings(True)

    # add some basic information to the log for debugging
    logger.debug(f"Setup root logger to save to: '{log_file}'.")
    logger.debug(f"Running on hostname: '{socket.gethostname()}'")
    logger.debug(f"Running on platform: '{platform.platform()}'")

    return logger
