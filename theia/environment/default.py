import arrow
from . import updaters


# Enviroment variables
ENV_VARIABLES = {}
ENV_VARIABLES["datetime"] = arrow.get(
    2018, 1, 1, 12, 0, 0, 0, tzinfo="Europe/Amsterdam"
)

# Enviroment settings
ENV_SETTINGS = {}
ENV_SETTINGS["time_factor"] = 10000
ENV_SETTINGS["country"] = "netherlands"
ENV_SETTINGS["latitude"] = 52.3
ENV_SETTINGS["longitude"] = 4.8
ENV_SETTINGS["altitude"] = -2

# Shop model
shops_model = updaters.StackedLinearModel("day")
shops_model.add_point(arrow.get("07:00", "HH:mm"), 0)
shops_model.add_point(arrow.get("10:00", "HH:mm"), 0.9)
shops_model.add_point(arrow.get("17:00", "HH:mm"), 0.9)
shops_model.add_point(arrow.get("22:00", "HH:mm"), 0)
ENV_SETTINGS["shops_model"] = shops_model
