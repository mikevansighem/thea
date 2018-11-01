class TheiaException(Exception):
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
