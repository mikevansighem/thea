import thing_updaters
from collections import namedtuple

# Values of the named tuple need to be of type: any, list of types, dict, callable
ThingType = namedtuple(
    "ThingType", ["default_value", "permitted_values", "default_properties", "updater"]
)

# A dictonary of all ThingTypes
THING_TYPES = {}
THING_TYPES["Shop"] = ThingType(
    default_value=False,
    permitted_values=[bool],
    default_properties={},
    updater=thing_updaters.shops,
)
