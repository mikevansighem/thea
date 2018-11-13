import pandas as pd
from pvlib.location import Location
from ..defenitions import env_updater
from arrow import Arrow
from typing import Dict


@env_updater
def solar_position(
    date_time: Arrow, latitude: float, longitude: float, altitude: float, temperature: float, pressure: float, **unused
) -> Dict[str, float]:

    location = Location(
        latitude=latitude,
        longitude=longitude,
        tz=date_time.datetime.tzname(),
        altitude=altitude,
    )
    times = pd.DatetimeIndex(start=date_time.datetime, periods=1, freq="1min")

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
