from pysolar.solar import get_altitude, get_azimuth


def solar_position(date_time, lattitude, longitude):
    """Returns solar position."""

    return (
        get_altitude(lattitude, longitude, date_time.datetime),
        get_azimuth(lattitude, longitude, date_time.datetime),
    )
