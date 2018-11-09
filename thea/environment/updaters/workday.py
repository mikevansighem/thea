"""Functions to determine weather it is a workday."""

import holidays


def workday(date_time, holiday, country: str) -> bool:
    """Returns a `bool` indicating if it is a workday."""

    if holiday is False:

        if (
            date_time.format("dddd") is "Saturday"
            or date_time.format("dddd") is "Sunday"
        ):
            # It is weekend
            return False
        else:
            # It is a workday
            return True
    else:
        # There is a holiday
        return False


def holiday(date_time, country: str):
    """If it is a holiday returns its name as a `str`."""

    holiday_calendar = holidays.CountryHoliday(country.upper())

    if date_time.date() in holiday_calendar:
        return holiday_calendar[date_time.date()]
    else:
        return False
