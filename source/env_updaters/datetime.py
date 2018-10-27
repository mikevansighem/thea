import arrow


def datetime(datetime, last_update, time_factor) -> None:
    """Updates date and time."""

    last_update, passed_time = arrow.utcnow(), arrow.utcnow() - last_update
    datetime = datetime + (passed_time * time_factor)

    try:
        real_update_rate = 1 / passed_time.total_seconds()
        sim_update_rate = 1 / (passed_time.total_seconds() * time_factor)

    except ZeroDivisionError:
        real_update_rate = 0
        sim_update_rate = 0

    return datetime, last_update, real_update_rate, sim_update_rate
