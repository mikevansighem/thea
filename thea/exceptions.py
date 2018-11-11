class TheaException(Exception):
    """Base Thea exception"""

    pass


class NoWorldError(TheaException):
    """Raise if no world has been loaded."""

    pass


class NameNotAvailable(TheaException):
    """Raise if the passed name is not available"""

    pass


class IgnoreSaved(TheaException):
    """Hack to raise when wanting to ignore the saved state."""

    pass


class CommNotConnectedError(TheaException):
    """Raise if a communicator is not connected."""

    pass


class MQTTError(TheaException):
    """Raise for errors related to the MQTT broker."""

    pass


class MQTTBrokerError(MQTTError):
    """Raise for errors related to the MQTT broker."""

    pass


class MQTTBrokerPortNotAvailible(MQTTError):
    """Raise if the MQTT broker port is not available."""

    pass
