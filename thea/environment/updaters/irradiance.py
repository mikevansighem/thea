import pandas as pd
from pvlib.location import Location
from ..defenitions import env_updater


@env_updater
def clearsky_irradiance(date_time, latitude, longitude, altitude, pressure, **unused):

    location = Location(
        latitude=latitude,
        longitude=longitude,
        tz=date_time.datetime.tzname(),
        altitude=altitude,
    )
    times = pd.DatetimeIndex(start=date_time.datetime, periods=1, freq="1min")

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
