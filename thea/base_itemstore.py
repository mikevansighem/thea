import warnings
from collections import namedtuple
from string import Template

from .exceptions import NameNotAvailable
from . import logger

# Type definition for BaseItem, used for tempting and testing only
BaseType = namedtuple("BaseType", ["default_properties"])
BASE_TYPES = {}
BASE_TYPES["Empty"] = BaseType(default_properties={})

# Name for creating an item without a specific name
BASEITEM_NAME_TEMPLATE = Template("$type_$number")


class BaseItem:
    """Object that can be stored in BaseStore."""

    # Define attributes that can be changed when inheriting this class
    type_dict = BASE_TYPES

    def __init__(self, type_: str, name: str, **kwargs) -> None:
        """Creates a new BaseItem instance."""

        # Set required type and name
        self.type_ = type_
        self.name = name

        # Add any other attributes defined in _additional_init
        kwargs = self._additional_attributes(**kwargs)

        # Overwrite default properties with passed properties
        self.properties = self.type_dict[self.type_].default_properties
        self.properties.update(**kwargs)

        # Handle remaining setup
        self._additional_init()

        logger.debug(f"Created or loaded {self}.")

    def __repr__(self) -> str:

        return f'An instance of {self.__class__.__name__} with type: "{self.type_}", name: "{self.name}" and {len(self.properties)} properties'

    def saveable_format(self) -> dict:
        """Returns a packable `dict` that can directly be passed into the init method to reinstanciate this object."""

        saveable_format = {}
        saveable_format["type_"] = self.type_
        saveable_format["name"] = self.name
        saveable_format["properties"] = self.properties

        saveable_format = {**saveable_format, **self._additional_saveable()}

        return saveable_format

    def _additional_attributes(self, **kwargs) -> dict:
        """Handles setting attributes not defined in the BaseItem class"""

        return kwargs

    def _additional_saveable(self) -> dict:
        """Handles saving attributes not defined in the BaseItem class"""

        saveable_format = {}

        return saveable_format

    def _additional_init(self) -> None:
        """Handles additional init after properties are set."""
        pass


class BaseStore:
    """A class that stores BaseItems by type."""

    # Define attributes that can be changed when inheriting this class
    item_to_create = BaseItem
    name_template = BASEITEM_NAME_TEMPLATE

    def __init__(self, items=[]):
        """Creates a new instance of this class."""

        # TODO make items private
        self.items = {}

        for saveable_item in items:
            self.new(**saveable_item)

        logger.debug(f"Created or loaded a {self}.")

    def __repr__(self):
        """Returns representation including number of stored items."""

        return f"An instance of {self.__class__.__name__} with {len(self)} items"

    def __len__(self):
        """Returns the number of items stored."""

        return len(self.get())

    def saveable_format(self) -> dict:
        """Returns a pickable `dict` that can directly be passed into the init method to reinstanciate this object."""

        saveable_items = []

        for item in self.get():
            saveable_item = item.saveable_state()
            saveable_items.append(saveable_item)

        saveable_state = {}
        saveable_state["items"] = saveable_items

        return saveable_state

    def _name_available(self, name: str) -> bool:
        """Returns `True` if the name is available."""

        for type_group, items in self.items.items():
            for item in items:
                if name == item.name:
                    return False

        return True

    def _generate_name(self, type_: str) -> str:
        """Returns the name with lowest available number."""

        counter = 0
        generated_name = self.name_template.substitute(type_=type_, number=counter)

        while not self._name_available(generated_name):

            generated_name = self.name_template.substitute(type_=type_, number=counter)
            counter += 1

        return generated_name

    def new(self, type_: str, **kwargs) -> None:
        """Create new item"""

        # Set name if none has been set and check if name is valid
        try:
            name = kwargs["name"]
            if self._name_available(name):
                kwargs.pop("name")
            else:
                raise NameNotAvailable(f'The name "{name}" is not available.')

        except KeyError:
            name = self._generate_name(type_)

        # Create item and add to items
        new_item = self.item_to_create(type_, name, **kwargs)

        # If type is not a key of stored items create it
        if type_ not in self.items:
            self.items[type_] = []

        # Store new item
        self.items[type_].append(new_item)

    def edit(self, name: str, **kwargs) -> None:
        """Edit item with `name`."""

        for type_group, items in self.items.items():
            for item in enumerate(items):
                if item.name == name:

                    # Get copy of old thing
                    old_item = item.saveable_format()

                    # Delete old thing
                    self.delete(name)

                    # Create new thing
                    old_item.update(kwargs)
                    self.new(**old_item)

                    logger.info(f"Edited {name} with {len(kwargs)-1} updated values.")

                    return

        raise KeyError(f"{name} could not be found in {self}.")

    def delete(self, name: str) -> None:
        """Remove value with `name` from the the store."""

        for type_group, items in self.items.items():
            for i, item in enumerate(items):
                if item.name == name:
                    del self.items[type_group][i]
                    return

        raise KeyError(f"{name} could not be found in {self}.")

    def get(self, type_=None, name=None, single_item=False) -> list:
        """Returns a list of all items matching the query."""

        # TODO make options

        output_list = []

        if type_ is None and name is None:
            for type_group, items in self.items.items():
                for item in items:
                    output_list.append(item)

        elif type_ is not None and name is None:
            output_list = self.items.get(type_, [])

        elif name is not None:
            for type_group, items in self.items.items():
                for item in items:
                    if item.name == name and (type_ is None or type_ == type_group):
                        output_list = [item]

        if len(output_list) == 0 and (type_ is not None or name is not None):
            raise KeyError(f"Could not find a match for query.")

        elif single_item is True and len(output_list) == 1:
            return output_list[0]

        elif single_item is True and len(output_list) != 1:
            raise warnings.warn("Only returned first item matching your query.")

        else:
            return output_list
