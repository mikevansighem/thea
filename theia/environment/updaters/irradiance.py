import pandas as pd
import pvlib
from pvlib.location import Location
import arrow


def clearsky_irradiance(datetime, latitude, longitude, altitude, pressure, **unused):

    location = Location(
        latitude=latitude,
        longitude=longitude,
        tz=datetime.datetime.tzname(),
        altitude=altitude,
    )
    times = pd.DatetimeIndex(start=datetime.datetime, periods=1, freq="1min")

    irradiance = location.get_clearsky(
        times, pressure=pressure
    )  # ineichen with climatology table by default
    ghi, dni, dhi = irradiance.values[0]
    irradiance = {
        "clear_sky_global_horizontal_irradiance": ghi,
        "clear_sky_direct_normal_irradiance": dni,
        "clear_sky_diffuse_horizontal_irradiance": dhi,
    }

    return irradiance
