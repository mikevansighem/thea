import arrow
from .default import ENV_SETTINGS, ENV_VARIABLES
from pretty_printing import pretty_string, pretty_dict
from . import updaters
import logging_setup

logger = logging_setup.aux_logger()


class Environment:
    def __init__(self, variables={}, settings={}) -> None:
        """Overwrites default values with passed values."""

        # Variables for updating the clock
        self._last_update = arrow.utcnow()
        self._real_update_rate = 0
        self._sim_update_rate = 0

        # Set settings
        self.settings = ENV_SETTINGS
        self.settings.update(settings)

        # Set variables according defaults and passed values
        self.variables = ENV_VARIABLES
        self.variables.update(variables)

        # Do update to calculate possibly missing variables
        self.update()

        # Set the non missing variables back to the passed values
        self.variables.update(variables)

        logger.debug(f"Created a new instance of {self}.")

    def __repr__(self) -> str:

        return f"An instance of {self.__class__.__name__} with {len(self.variables)} variables and {len(self.settings)} settings"

    def saveable_format(self) -> dict:

        saveable_format = {}
        saveable_format["variables"] = self.variables
        saveable_format["settings"] = self.settings

        return saveable_format

    def update(self) -> None:
        """Updates variables based on the settings and other variables"""

        # Add not yet being calculated variables
        self.variables["temperature"] = 12
        self.variables["pressure"] = None

        # First update date-time because everything is dependent on it
        self.variables[
            "datetime"
        ], self._last_update, self._real_update_rate, self._sim_update_rate = updaters.datetime(
            self.variables["datetime"], self._last_update, self.settings["time_factor"]
        )

        # Next edit variables solely dependent upon date-time (and/or settings)
        self.variables["season"] = updaters.season(self.variables["datetime"])
        self.variables["workday"] = updaters.workday(
            self.variables["datetime"], self.settings["country"]
        )
        self.variables["holiday"] = updaters.holiday(
            self.variables["datetime"], self.settings["country"]
        )
        self.variables["shops_open"] = self.settings["shops_model"].get_value(
            self.variables["datetime"]
        )

        # Next edit variables dependent on other variables (and/or settings)
        self.variables.update(
            updaters.solar_position(**self.settings, **self.variables)
        )
        self.variables.update(
            updaters.clearsky_irradiance(**self.settings, **self.variables)
        )

        # Update variables dependent on previous (and/or settings)
        self.variables["solar_wind_direction"] = updaters.angle_to_winddirection(
            self.variables["solar_azimuth"]
        )

    def change_settings(self, new_settings):
        """Updates environment settings."""

        self.settings.update(new_settings)
        logger.info(
            f"Updated settings of {self} with {len(new_settings)} new or changed values."
        )

    def print(self) -> None:
        """Print an overview of the current environment."""

        logger.info("===========")
        logger.info("environment")
        logger.info("===========")

        logger.info("Last Update: {}".format(self._last_update.time()))
        logger.info(
            "Real Update Rate: {}".format(pretty_string(self._real_update_rate))
        )
        logger.info("Sim Update Rate: {}".format(pretty_string(self._sim_update_rate)))

        self.print_settings()
        self.print_values()

    def print_settings(self) -> None:
        """Prints all environment variables."""

        logger.info("--------------------")
        logger.info("ENVIRONMENT SETTINGS")
        logger.info("--------------------")

        pretty_settings = pretty_dict(self.settings)
        for key in pretty_settings:
            logger.info("{}: {}".format(key, pretty_settings[key]))

    def print_values(self) -> None:
        """Prints all environment variables."""

        logger.info("---------------------")
        logger.info("ENVIRONMENT VARIABLES")
        logger.info("---------------------")

        pretty_settings = pretty_dict(self.variables)
        for key in pretty_settings:
            logger.info("{}: {}".format(key, pretty_settings[key]))
