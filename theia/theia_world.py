from .environment import Environment
from .things import ThingsStore
from .communicators import CommunicatorStore
from .env_thing_linker import EnvThingsLinker
from . import logger


class TheiaWorld:
    def __init__(self):

        self.world_loaded = False
        logger.warning("Created unload world")

    def _check_loaded(self):

        if self.world_loaded is False:
            raise Exception("No Theia world has been loaded.")

    def new(self):
        """Create new world."""

        self.environment = Environment()
        self.things = ThingsStore()
        self.communicators = CommunicatorStore()
        self.env_thing_linker = EnvThingsLinker()

        self.world_loaded = True

    def save(self):
        """Save current world to file."""

        self._check_loaded()

    def load(self):
        """Load a world from file."""

        self.loaded = True

    def update(self):
        """Update world."""

        self._check_loaded()

        self.environment.update()
        self.env_thing_linker.update(self.things.items, self.environment.variables)
