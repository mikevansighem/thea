from thing_types import THING_TYPES
from thing_types import ThingType

def test_thing_type_defenitions():

    for key, item in THING_TYPES.items():

        # Check if it is a ThingType
        assert isinstance(item, ThingType)

        # Check if a default value has been set
        assert item.default_value is not None

        # Check if it is a list of types    
        assert isinstance(item.permitted_values, list)
        for item_in_list in item.permitted_values:
            assert isinstance(item_in_list, type)

        # Check if dict
        assert isinstance(item.default_properties, dict)

        # Check if function
        assert hasattr(item.updater, '__call__')
