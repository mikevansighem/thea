from . import logger


class BinaryOut:
    def __init__(self, pin):
        self.pin = pin

    def set(self, value, diasable=False):
        logger.info(f'Binary output on pin "{self.pin}" set to "{value}".')


class AnalogOut:
    def __init__(self, pin):
        self.pin = pin

    def set(self, value, diasable=False):
        logger.info(f'Analog output on pin "{self.pin}" set to "{value}".')


"""Hardware types where the first item is the endpoint and the second is
the method to set the value on a specific hardware pin."""

HARDWARE_TYPES = {
    "pi_binary_out": {
        0: BinaryOut(0).set,
        1: BinaryOut(1).set,
        2: BinaryOut(2).set,
        3: BinaryOut(3).set,
        4: BinaryOut(4).set,
        5: BinaryOut(5).set,
    },
    "pi_analog_out": {
        0: AnalogOut(0).set,
        1: AnalogOut(1).set,
        2: AnalogOut(2).set,
        3: AnalogOut(3).set,
        4: AnalogOut(4).set,
        5: AnalogOut(5).set,
    },
    "pi_mixed": {
        0: AnalogOut(0).set,
        1: AnalogOut(1).set,
        2: BinaryOut(2).set,
        3: BinaryOut(3).set,
        4: AnalogOut(4).set,
        5: BinaryOut(5).set,
    },
}
