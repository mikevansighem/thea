from base_itemstore import BaseItem, BaseStore
from communiactor_types import COMMUNICATOR_TYPES


class Communicator(BaseItem):
    """A communicator is a object that connects with hardware."""

    # Define attributes that should be changed when inheriting this class
    type_dict = COMMUNICATOR_TYPES

    def _additional_init(self, **kwargs) -> dict:
        """Handles setting atributes not defined in the BaseItem class"""

        # Set value to default if it has not been passed
        self.value = kwargs.get("value", self.type_dict[self.type_].default_value)
        kwargs.pop("value")

        return kwargs

    def _additional_saveable(self) -> dict:
        """Handles saving atributes not defined in the BaseItem class"""

        saveable_format = {}

        return saveable_format


class CommunicatorStore(BaseStore):

    item_to_create = Communicator
