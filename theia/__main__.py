"""
Currently implemented in main:
- Start default environment
- Create empty things store
- Link environment to things
- Run environment
- Run environment things linker
"""

import logging_setup
from environment import Environment
from things import ThingsStore
from communicators import CommunicatorStore
from env_thing_linker import EnvThingsLinker

logger = logging_setup.aux_logger()


def main():

    # Create base classes
    environment = Environment()
    things_store = ThingsStore()
    communicator_store = CommunicatorStore()
    env_thing_linker = EnvThingsLinker()

    # Add some entries to the stores
    things_store.new("shop")
    communicator_store.new("mqtt")

    while True:

        # Update environment
        environment.update()
        environment.print()

        # Update things
        env_thing_linker.update(things_store.items, environment.variables)


if __name__ == "__main__":

    main()
