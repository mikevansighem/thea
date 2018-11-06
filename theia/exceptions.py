class TheiaException(Exception):
    """Base Theia exception"""

    pass


class NoWorldError(TheiaException):
    """Raise if no world has been loaded."""

    pass


class NameNotAvailable(TheiaException):
    """Raise if the passed name is not available"""

    pass


class CommNotConnectedError(TheiaException):
    """Raise if a communicator is not connected."""

    pass


class MQTTBrokerError(TheiaException):
    """Raise for errors related to the MQTT broker."""

    pass


class MQTTBrokerPortNotAvailible(TheiaException):
    """Raise if the MQTT broker port is not available."""

    pass


class IgnoreSaved(TheiaException):
    """Hack to raise when wanting to ignore the saved state."""

    pass
