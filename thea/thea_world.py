import pickle
import logging

from .environment import Environment
from .things import ThingsStore
from .communicators import CommunicatorStore
from .env_thing_linker import EnvThingsLinker
from .exceptions import NoWorldError

logger = logging.getLogger(__name__)


def check_world_loaded(function):
    """Decorator to check if a Thea world has been loaded/created."""

    def wrapper(*args, **kwargs):
        if args[0].world_loaded is False:
            raise NoWorldError(
                f'No Thea world loaded, cannot execute: "{function.__name__}".'
            )
        else:
            return function(*args, **kwargs)

    return wrapper


class TheaWorld:
    def __init__(self):

        self.world_loaded = False

    def new(self, name):
        """Create new world."""

        # Saveables
        self._name = name
        self._environment = Environment()
        self._things = ThingsStore()
        self._communicators = CommunicatorStore()

        # Non-saveables
        self._env_thing_linker = EnvThingsLinker()

        # Indicate a world has been loaded
        self.world_loaded = True

        logger.info(f'Created new Thea world named: "{self._name}".')

    @check_world_loaded
    def save(self, file_name=""):
        """Save current world to file."""

        if file_name is "":
            file = f"{self._name.replace(' ','_').lower()}.tw"
        else:
            file = f"{file_name}.tw"

        # Add all objects to dictionary to be pickled
        saveable_world = {}
        saveable_world["name"] = self.name
        saveable_world["environment"] = self.environment.saveable_format()
        saveable_world["things"] = self.things.saveable_format()
        saveable_world["communicators"] = self.communicators.saveable_format()

        pickle.dump(saveable_world, open(file, "wb"))

        logger.info(f'Saved Thea world named "{self._name}" to "{file}".')

    def load(self, file):
        """Load a world from file."""

        loaded_world = pickle.load(open(file, "rb"))
        self._name = loaded_world["name"]
        self._environment = Environment(**loaded_world["environment"])
        self._things = ThingsStore(**loaded_world["things"])
        self._communicators = CommunicatorStore(**loaded_world["communicators"])

        # Non-saveables
        self._env_thing_linker = EnvThingsLinker()

        # Indicate a world has been loaded
        self.loaded = True

        logger.info(f'Loaded Thea world named "{self._name}" from "{file}".')

    @check_world_loaded
    def update(self):
        """Update world."""

        self.environment.update()
        self.env_thing_linker.update(self.things.items, self.environment.properties)

    @property
    def name(self):
        """This attribute is a property so we can check if a Thea world has been loaded."""

        try:
            return self._name
        except AttributeError:
            raise NoWorldError(f'No Thea world loaded, cannot access "name".')

    @property
    def environment(self):
        """This attribute is a property so we can check if a Thea world has been loaded."""

        try:
            return self._environment
        except AttributeError:
            raise NoWorldError(f'No Thea world loaded, cannot access "environment".')

    @property
    def things(self):
        """This attribute is a property so we can check if a Thea world has been loaded."""

        try:
            return self._things
        except AttributeError:
            raise NoWorldError(f'No Thea world loaded, cannot access "things".')

    @property
    def communicators(self):
        """This attribute is a property so we can check if a Thea world has been loaded."""

        try:
            return self._communicators
        except AttributeError:
            raise NoWorldError(f'No Thea world loaded, cannot access "communicators".')

    @property
    def env_thing_linker(self):
        """This attribute is a property so we can check if a Thea world has been loaded."""

        try:
            return self._env_thing_linker
        except AttributeError:
            raise NoWorldError(
                f'No Thea world loaded, cannot access "env_thing_linker".'
            )
