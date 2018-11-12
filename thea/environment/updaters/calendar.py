import holidays
from ..defenitions import env_updater

SPRING = range(80, 172)
SUMMER = range(172, 264)
FALL = range(264, 355)
# WINTER = everything else


@env_updater
def season(date_time, **unused) -> str:
    """Returns the current season."""

    day_of_year = int(date_time.format("DDDD"))

    if day_of_year in SPRING:
        season = "spring"
    elif day_of_year in SUMMER:
        season = "summer"
    elif day_of_year in FALL:
        season = "fall"
    else:
        season = "winter"

    return {"season": season}


@env_updater
def workday(date_time, holiday, country: str, **unused) -> bool:
    """Returns a `bool` indicating if it is a workday."""

    if holiday is False:

        if (
            date_time.format("dddd") is "Saturday"
            or date_time.format("dddd") is "Sunday"
        ):
            # It is weekend
            return_value = False
        else:
            # It is a workday
            return_value = True
    else:
        # There is a holiday
        return_value = False

    return {"workday": return_value}


@env_updater
def holiday(date_time, country: str, **unused):
    """If it is a holiday returns its name as a `str`."""

    holiday_calendar = holidays.CountryHoliday(country.upper())

    if date_time.date() in holiday_calendar:
        return_value = holiday_calendar[date_time.date()]
    else:
        return_value = False

    return {"holiday": return_value}
