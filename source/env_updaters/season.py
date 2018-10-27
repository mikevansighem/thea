SPRING = range(80, 172)
SUMMER = range(172, 264)
FALL = range(264, 355)
# winter = everything else


def season(date_time) -> str:
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

    return season
