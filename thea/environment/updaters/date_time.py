import arrow
from arrow import Arrow
from ..defenitions import env_updater
from typing import Dict, Union


@env_updater
def date_time(date_time, _last_update, time_factor, **unused) -> Dict[str, Union[Arrow, float]]:
    """Updates date and time."""

    _last_update, passed_time = arrow.utcnow(), arrow.utcnow() - _last_update
    date_time = date_time + (passed_time * time_factor)

    try:
        real_update_rate = 1 / passed_time.total_seconds()
        sim_update_rate = 1 / (passed_time.total_seconds() * time_factor)

    except ZeroDivisionError:
        real_update_rate = 0
        sim_update_rate = 0

    return {
        "date_time": date_time,
        "_last_update": _last_update,
        "_real_update_rate": real_update_rate,
        "_sim_update_rate": sim_update_rate,
    }
