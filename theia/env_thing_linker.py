from thing_types import THING_TYPES


class EnvThingsLinker:
    @staticmethod
    def update(things_by_type, env_variables):

        for thing_type, things in things_by_type.items():

            THING_TYPES[thing_type].updater(
                things_of_single_type=things, **env_variables
            )
