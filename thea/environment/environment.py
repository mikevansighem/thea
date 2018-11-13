import logging
from . import updaters
from .defenitions import ENV_PROPERTIES

logger = logging.getLogger(__name__)


class Environment:
    def __init__(self, properties=None) -> None:
        """Overwrites default values with passed values."""

        self.properties = ENV_PROPERTIES
        if properties is not None:
            self.properties.update(properties)

        # Do an update so all fields will be populated
        self.update()

        logger.debug(f"Created a new instance of '{self}'.")

    def __repr__(self) -> str:

        return f"an instance of {self.__class__.__name__} with {len(self.properties)} properties"

    def saveable_format(self) -> dict:

        saveable_format = {}
        saveable_format["properties"] = self.properties

        return saveable_format

    def update(self):
        """Updates all properties that are not fixed."""

        # First update date-time because everything is dependent on it
        self.properties = updaters.date_time(**self.properties)

        # Next edit variables solely dependent upon date-time (and/or settings)
        self.properties = updaters.season(**self.properties)
        self.properties = updaters.holiday(**self.properties)

        # TODO
        self.properties["shops_open"].value = self.properties[
            "shops_model"
        ].value.get_value(self.properties["date_time"].value)

        # Next edit variables dependent on other variables (and/or settings)
        self.properties = updaters.workday(**self.properties)
        self.properties = updaters.solar_position(**self.properties)
        self.properties = updaters.clearsky_irradiance(**self.properties)

        # Update variables dependent on previous (and/or settings)
        self.properties = updaters.solar_wind_direction(**self.properties)

    def change_property(self, new_properties):
        """Updates environment settings."""

        self.properties.update(new_properties)
        logger.info(
            f"Updated properties of '{self}' with {len(new_properties)} new or changed values."
        )

    def print(self) -> None:
        """Print an overview of the current environment."""

        logger.info("===========")
        logger.info("environment")
        logger.info("===========")

        for _key, property_ in self.properties.items():
            logger.info(str(property_))
