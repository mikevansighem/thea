"""Updates the value of things using the thing updater informed by environment variables."""

from .thing_types import THING_TYPES


class EnvThingsLinker:
    """Handles linking of things and things updater's."""

    @staticmethod
    def update(things_by_type, env_properties):
        """Updates all types using their matching updater."""

        env_property_values = {}
        for key, item in env_properties.items():
            env_property_values[key] = item.value

        # Loop over all types
        # TODO stop using .items() but a native implementation
        for thing_type, things in things_by_type.items():

            # Retrieve updater from thing definition and pass it all
            # things matching the type as well as all env variables.
            THING_TYPES[thing_type].updater(
                things_of_single_type=things, **env_property_values
            )
