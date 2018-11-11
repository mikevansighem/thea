"""Checks thing type definitions"""

from thea.thing_types import THING_TYPES
from thea.thing_types import ThingType


def test_is_thing_type():
    """Check if instance of ThingType"""

    for _key, item in THING_TYPES.items():
        assert isinstance(item, ThingType)


def test_permitted_values_iterable():
    """Permitted value is type or range."""

    for _key, item in THING_TYPES.items():
        for item_in_list in item.permitted_values:
            assert isinstance(item_in_list, type) or isinstance(item_in_list, type)


def test_properties_are_dict():
    """Properties are a dictionary.."""

    for _key, item in THING_TYPES.items():
        assert isinstance(item.default_properties, dict)


def test_updater_is_callable():
    """Updater needs to be callable."""

    for _key, item in THING_TYPES.items():
        assert callable(item.updater)
