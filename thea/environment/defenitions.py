"""Definitions for the environment properties.

An environment property can be anything one could use to describe an
element of the environment. They can be constant (eg location) or variable
(eg temperature).

They are stored in the EnvProperty class for easy reference to units,
defaults and descriptions.

All the default properties are based on those for Amsterdam.
"""

import arrow
from arrow import Arrow
from .updaters.stacked_linear_model import StackedLinearModel
from typing import Callable, Dict


def env_updater(func: Callable):
    """A wrapper to retrieve and set values in a dictionary of EnvSettings"""

    def wrapper(**kwargs) -> Dict[str, str]:

        values = {}
        for key, item in kwargs.items():
            values[key] = item.value

        # Call the updater
        return_dict = func(**values)

        for key, item in return_dict.items():
            kwargs[key].value = item

        return kwargs

    return wrapper


class EnvProperty:
    """A class to store all information on an environment setting"""

    def __init__(
        self,
        name,
        help_,
        allowed=None,
        long_unit="",
        short_unit="",
        default=None,
        value=None,
        constant=False,
    ):
        """Stores all attributes."""

        self.name = name
        self.long_unit = long_unit
        self.short_unit = short_unit
        self.allowed = allowed
        self.help_ = help_
        self.default = default
        self.constant = constant

        # If there is no default (or start value) set it to None
        if default is not None:
            self.default = default

        if value is None:
            self.value = self.default
        else:
            self.value = value

        # TODO add value setter for value where it is checked against allowed and constant

    def __repr__(self) -> str:
        return (
            f"an instance of EnvProperty with "
            f"name: '{self.name}', "
            f"long_unit: '{self.long_unit}', "
            f"short_unit: '{self.short_unit}', "
            f"allowed: '{self.allowed}', "
            f"default: '{self.default}', "
            f"help_: '{self.help_}', "
            f"value: '{self.value}'"
        )

    def __str__(self) -> str:

        if isinstance(self.value, float):
            value = round(self.value, 2)
        else:
            value = self.value

        return f"{self.name}: {value} {self.long_unit}"


ENV_PROPERTIES = {}

ENV_PROPERTIES["date_time"] = EnvProperty(
    name="Date and time",
    allowed=Arrow,
    default=arrow.get(2018, 1, 1, 12, 0, 0, 0, tzinfo="Europe/Amsterdam"),
    help_="Date and time.",
)

ENV_PROPERTIES["_last_update"] = EnvProperty(
    name="Last environment update",
    allowed=Arrow,
    default=arrow.utcnow(),
    help_="Last date and time the environment was updated.",
)

ENV_PROPERTIES["_real_update_rate"] = EnvProperty(
    name="Real update rate",
    long_unit="times per second",
    short_unit="x/s",
    help_="Times the environment is updated per second according to real world time.",
)

ENV_PROPERTIES["_sim_update_rate"] = EnvProperty(
    name="Environment simulation update rate",
    long_unit="times per second",
    short_unit="x/s",
    help_="Times the environment is updated per second according to environment time.",
)

ENV_PROPERTIES["time_factor"] = EnvProperty(
    name="Time-factor",
    long_unit="times",
    short_unit="x",
    allowed=range(1, 100_000),
    default=1000,
    help_="Factor time will be sped up.",
)

ENV_PROPERTIES["altitude"] = EnvProperty(
    name="Altitude",
    long_unit="meters",
    short_unit="m",
    allowed=range(-100, 2000),
    default=-2,
    help_="Altitude of the location in meters.",
)

ENV_PROPERTIES["latitude"] = EnvProperty(
    name="Latitude",
    long_unit="degrees",
    short_unit="°",
    allowed=range(-90, 90),
    default=52.370216,
    help_="Latitude of the location in degrees.",
)

ENV_PROPERTIES["longitude"] = EnvProperty(
    name="Longitude",
    long_unit="degrees",
    short_unit="°",
    allowed=range(-180, 180),
    default=4.895168,
    help_="Longitude of the location in degrees.",
)

ENV_PROPERTIES["country"] = EnvProperty(
    name="Country",
    allowed=str,
    default="NL",
    help_="ISO 3166 2-character country code.",
)

shops_model = StackedLinearModel("day")
shops_model.add_point(arrow.get("07:00", "HH:mm"), 0)
shops_model.add_point(arrow.get("10:00", "HH:mm"), 0.9)
shops_model.add_point(arrow.get("17:00", "HH:mm"), 0.9)
shops_model.add_point(arrow.get("22:00", "HH:mm"), 0)

ENV_PROPERTIES["shops_model"] = EnvProperty(
    name="Shops model",
    allowed=StackedLinearModel,
    default=shops_model,
    help_="Model to use for opening/closing shops",
    constant=True,
)

ENV_PROPERTIES["shops_open"] = EnvProperty(
    name="Shops open",
    long_unit="out of of 1.0",
    allowed=range(0, 1),
    help_="Fraction of the shops open.",
)

ENV_PROPERTIES["temperature"] = EnvProperty(
    name="Temperature",
    long_unit="degrees Celsius",
    short_unit="°C",
    allowed=float,
    default=12,
    help_="Temperature in degrees Celsius.",
)

ENV_PROPERTIES["solar_wind_direction"] = EnvProperty(
    name="Solar wind-direction",
    allowed=str,
    help_="Solar position as a wind-direction.",
)

ENV_PROPERTIES["apparent_solar_zenith"] = EnvProperty(
    name="Apparent solar zenith",
    long_unit="degrees",
    short_unit="°",
    help_="Apparent zenith of the sun in degrees.",
)

ENV_PROPERTIES["solar_zenith"] = EnvProperty(
    name="Solar zenith",
    long_unit="degrees",
    short_unit="°",
    help_="Zenith of the sun in degrees.",
)

ENV_PROPERTIES["apparent_solar_elevation"] = EnvProperty(
    name="Apparent solar elevation",
    long_unit="meters",
    short_unit="m",
    help_="Apparent elevation of the sun in meters.",
)

ENV_PROPERTIES["solar_elevation"] = EnvProperty(
    name="Solar elevation",
    long_unit="meters",
    short_unit="m",
    help_="Elevation of the sun in meters.",
)

ENV_PROPERTIES["solar_azimuth"] = EnvProperty(
    name="Solar azimuth",
    long_unit="degrees",
    short_unit="°",
    help_="Azimuth of the sun in degrees.",
)

ENV_PROPERTIES["equation_of_time"] = EnvProperty(
    name="Equation of time",
    long_unit="minutes",
    short_unit="min",
    help_="Difference in time between solar time and mean solar time in minutes.",
)

ENV_PROPERTIES["pressure"] = EnvProperty(
    name="Solar azimuth",
    long_unit="pascal",
    short_unit="Pa",
    default=None,  # TODO make variable
    help_="The pressure in Pascal.",
)

ENV_PROPERTIES["holiday"] = EnvProperty(
    name="Holiday", help_="Name of the current holiday."
)

ENV_PROPERTIES["workday"] = EnvProperty(
    name="Workday", help_="Whether it is a workday."
)

ENV_PROPERTIES["season"] = EnvProperty(name="Season", help_="Season of the year.")


ENV_PROPERTIES["clear_sky_global_horizontal_irradiance"] = EnvProperty(
    name="Clear sky global horizontal irradiance",
    long_unit="watt per square meter",
    short_unit="W/m^2",
    help_="The clear sky global horizontal irradiance in watt per square meter.",
)

ENV_PROPERTIES["clear_sky_direct_normal_irradiance"] = EnvProperty(
    name="Clear sky direct normal irradiance",
    long_unit="watt per square meter",
    short_unit="W/m^2",
    help_="The clear sky direct normal irradiance in watt per square meter.",
)

ENV_PROPERTIES["clear_sky_diffuse_horizontal_irradiance"] = EnvProperty(
    name="Clear sky diffuse horizontal irradiance",
    long_unit="watt per square meter",
    short_unit="W/m^2",
    help_="The clear sky diffuse horizontal irradiance in watt per square meter.",
)
