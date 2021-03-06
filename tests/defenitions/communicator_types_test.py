"""Checks communicator type definitions"""

from thea.communicator_types import COMMUNICATOR_TYPES
from thea.communicator_types import CommunicatorType


def test_is_thing_type():
    """Check if instance of CommunicatorType"""

    for _key, item in COMMUNICATOR_TYPES.items():
        assert isinstance(item, CommunicatorType)


def test_properties_are_dict():
    """Properties are a dictionary.."""

    for _key, item in COMMUNICATOR_TYPES.items():
        assert isinstance(item.default_properties, dict)


def test_comm_handler_is_callable():
    """comm_handlers needs to be callable."""

    for _key, item in COMMUNICATOR_TYPES.items():
        assert callable(item.comm_handler)
