import pandas as pd
from pvlib.location import Location


def solar_position(
    datetime, latitude, longitude, altitude, temperature, pressure, **unused
):

    location = Location(
        latitude=latitude,
        longitude=longitude,
        tz=datetime.datetime.tzname(),
        altitude=altitude,
    )
    times = pd.DatetimeIndex(start=datetime.datetime, periods=1, freq="1min")

    packed = location.get_solarposition(
        times, pressure=pressure, temperature=temperature
    )
    apparent_zenith, zenith, apparent_elevation, elevation, azimuth, equation_of_time = packed.values[
        0
    ]

    solar_position = {
        "apparent_solar_zenith": apparent_zenith,
        "solar_zenith": zenith,
        "apparent_solar_elevation": apparent_elevation,
        "solar_elevation": elevation,
        "solar_azimuth": azimuth,
        "equation_of_time": equation_of_time,
    }
    return solar_position
