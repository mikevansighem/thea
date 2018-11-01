import workalendar
from datetime import date
from workalendar.europe import *

LOCAL_CALENDAR = {
    "netherlands": Netherlands(),
    "germany": Germany(),
    "france": France(),
    "belgium": Belgium(),
}


def workday(date_time, country: str) -> bool:
    """Returns a `bool` indicating if it is a workday."""

    holiday_calendar = LOCAL_CALENDAR[country.lower()]

    return holiday_calendar.is_working_day(date_time.date())


def holiday(date_time, country: str):
    """If it is a holiday returns its name as a `str`."""

    holiday_calendar = LOCAL_CALENDAR[country.lower()]
    holidays = holiday_calendar.holidays(date_time.year)

    if date_time.date() in holidays:
        return holidays[date_time.date()]
    else:
        return None
