"""Functions to convert environment variables to a human-comprehensible format."""

from ..defenitions import env_updater

WINDDIRECTIONS = {
    0: "N",
    1: "NNE",
    2: "NE",
    3: "ENE",
    4: "E",
    5: "ESE",
    6: "SE",
    7: "SSE",
    8: "S",
    9: "SSW",
    10: "SW",
    11: "WSW",
    12: "W",
    13: "WNW",
    14: "NW",
    15: "NNW",
    16: "N",
}


def angle_to_winddirection(angle):
    """Returns the wind-direction of a given angle as a `str`."""

    lookup = int((angle + 11.25) / 22.5)
    return WINDDIRECTIONS[lookup]


@env_updater
def solar_wind_direction(solar_azimuth, **unused):

    return {"solar_wind_direction": angle_to_winddirection(solar_azimuth)}
