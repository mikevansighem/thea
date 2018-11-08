class TheaException(Exception):
    """Base Thea exception"""

    pass


class NoWorldError(TheaException):
    """Raise if no world has been loaded."""

    pass


class NameNotAvailable(TheaException):
    """Raise if the passed name is not available"""

    pass


class CommNotConnectedError(TheaException):
    """Raise if a communicator is not connected."""

    pass


class MQTTBrokerError(TheaException):
    """Raise for errors related to the MQTT broker."""

    pass


class MQTTBrokerPortNotAvailible(TheaException):
    """Raise if the MQTT broker port is not available."""

    pass


class IgnoreSaved(TheaException):
    """Hack to raise when wanting to ignore the saved state."""

    pass
