"""
Currently implemented in main:
- Start default environment
- Create empty things store
- Link environment to things
- Run environment
- Run environment things linker
"""

from environment import Environment
from things import ThingsStore
from env_thing_linker import EnvThingsLinker


def main():

    environment = Environment()
    things_store = ThingsStore()
    env_thing_linker = EnvThingsLinker()

    while True:

        # Update environment
        environment.update()
        environment.print()

        # Update things
        env_thing_linker.update(things_store.items, environment.variables)


if __name__ == "__main__":

    main()
