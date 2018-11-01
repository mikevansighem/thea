"""A set of functions for printing data in a esthetically pleasing way"""


def pretty_string(value):
    """Reformats any data-type to a formatted string for printing."""

    # Prevent empty spot
    if value is None:
        value = "None"

    # Limiting decimal numbers for floats
    elif isinstance(value, float):
        value = str(round(value, 2))

    # Remove "_" and capitalize
    elif isinstance(value, str):

        value = value.replace("_", " ")

        # When all lower case convert to title case
        if value.islower():
            value = value.title()

    # Catch everything else with simple conversion
    else:
        value = str(value)

    return value


def pretty_dict(dictonary):
    """Formats dictionary with `pretty_string`."""

    pretty_dictonary = {}
    for key in dictonary:
        pretty_dictonary[pretty_string(key)] = pretty_string(dictonary[key])

    return pretty_dictonary
