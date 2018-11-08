# Shops Model: StackedLinearModel with 4 datapoints
# ---------------------
# Datetime: 2018-11-04T08:43:37.208913+00:00
# Temperature: 12
# Pressure: None
# Season: Fall
# Workday: False
# Holiday: None
# Shops Open: 0.52
# Apparent Solar Zenith: 76.03
# Solar Zenith: 76.09
# Apparent Solar Elevation: 13.97
# Solar Elevation: 13.91
# Solar Azimuth: 140.14
# Equation Of Time: 16.45
# Clear Sky Global Horizontal Irradiance: 185.33
# Clear Sky Direct Normal Irradiance: 579.49
# Clear Sky Diffuse Horizontal Irradiance: 45.41
# Solar Wind Direction: SE

"""Definitions for the environment settings and variables."""

from collections import namedtuple

"""Environment setting"""

EnvSetting = namedtuple(
    "EnvSetting", ["name", "long_unit", "short_unit", "allowed", "default", "help_"]
)
ENV_SETTINGS_DEF = {}

ENV_SETTINGS_DEF["time_factor"] = EnvSetting(
    name="Time-factor",
    long_unit="times",
    short_unit="x",
    allowed=range(1, 100_000),
    default=1000,
    help_="Factor time will be sped up.",
)

ENV_SETTINGS_DEF["altitude"] = EnvSetting(
    name="Altitude",
    long_unit="meters",
    short_unit="m",
    allowed=range(-100, 2000),
    default=0,
    help_="Altitude of the location in meters.",
)

ENV_SETTINGS_DEF["latitude"] = EnvSetting(
    name="Latitude",
    long_unit="degrees",
    short_unit="°",
    allowed=range(-90, 90),
    default=52.3,
    help_="Latitude of the location in degrees.",
)

ENV_SETTINGS_DEF["longitude"] = EnvSetting(
    name="Longitude",
    long_unit="degrees",
    short_unit="°",
    allowed=range(-180, 180),
    default=4.8,
    help_="Longitude of the location in degrees.",
)

ENV_SETTINGS_DEF["country"] = EnvSetting(
    name="Country",
    long_unit="",
    short_unit="",
    allowed=str,
    default="NL",
    help_="ISO 3166 2-character country code.",
)


"""Environment variables"""

EnvVariable = namedtuple("EnvVariable", ["unit", "help_"])
ENV_VARIABLES_DEF = {}

ENV_VARIABLES_DEF["temperature"] = EnvVariable(
    name="Temperature",
    long_unit="degrees Celsius",
    short_unit="°C",
    help_="Temperature in degrees Celsius.",
)
