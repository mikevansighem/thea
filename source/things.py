from base_itemstore import BaseItem, BaseStore
from thing_types import THING_TYPES

class Thing(BaseItem):
    """A thing is somthing that can be controlled."""

    # Define attributes that can be changed when inheriting this class
    type_dict = THING_TYPES
    

    def _additional_init(self, **kwargs) -> dict:
        """Handles setting atributes not defined in the BaseItem class"""

        # Set value to default if it has not been passed
        self.value = kwargs.get('value', self.type_dict[self.type_].default_value)

        # Remove value so it does not end up in the properties
        kwargs.pop('value')

        return kwargs

    def _additional_saveable(self) -> dict:
        """Handles saving atributes not defined in the BaseItem class"""

        saveable_format = {}
        saveable_format['value'] = {}

        return saveable_format


    @property
    def value(self, value):
        """Returns the value."""

        return self._value    

    @value.setter
    def value(self):
        """Checks value for correct `type` and propagates value change to hardware."""

        if type(value) in THING_TYPES[self.type_].permitted_values:
            self._value = value

            # TODO: Propagate value change to hardware
            
        else:
            raise ValueError(f'"{type(value)}" is not a valid value type for a "{self.type}".')

    def __str__(self) -> str:

        return f'A {self.type_} named "{self.name}" with value "{self.value}"'  



class ThingsStore(BaseStore):

    item_to_create = Thing


