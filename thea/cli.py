import argparse
import warnings
import logging

from .thea_world import TheaWorld
from . import logger


def cli_main():
    """Function to try out common Thea commands."""

    warnings.warn("The CLI-app is not ready yet and is currently used for debugging.")

    # Setup new Thea Wrapper
    tw = TheaWorld()
    tw.new("test world")
    tw.save("hi")
    tw.load("hi.tw")

    # Add some things
    for i in range(0, 5):
        tw.things.new(type_="shop")

    # Show the things
    # print(tw.things.get())

    # Add a communicator
    tw.communicators.new(type_="mqtt")

    # Connect the communicator
    comm = tw.communicators.get(name="mqtt0", single_item=True)
    print(comm.status)
    comm.connect()
    print(comm.status)
    comm.disconnect()
    print(comm.status)
    comm.connect()
    print(comm.status)

    while True:

        # Update environment
        tw.update()
        # tw.environment.print()


def cli_app():
    """Handles initial argument to start main."""

    logger.info("Started the Thea command-line application.")

    parser = argparse.ArgumentParser(description="Start Thea.")
    parser.add_argument(
        "-v", "--verbose", help="Verbose printing.", action="store_true"
    )
    args = parser.parse_args()

    # Force debug logging TODO remove
    args.verbose = True

    # Set verbosity level of logger
    if args.verbose is True:
        logger.parent.handlers[0].setLevel(logging.DEBUG)
    else:
        logger.parent.handlers[0].setLevel(logging.INFO)

    # Start main
    cli_main()


if __name__ == "__main__":
    cli_app()
