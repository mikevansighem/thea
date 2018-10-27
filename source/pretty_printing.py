def pretty_string(value):

    if value is None:
        value = "None"
    elif isinstance(value, float):
        value = str(round(value, 2))
    elif isinstance(value, str):
        value = value.replace("_", " ").title()
    else:
        value = str(value)

    return value


def pretty_dict(dictonary):

    pretty_dictonary = {}
    for key in dictonary:
        pretty_dictonary[pretty_string(key)] = pretty_string(dictonary[key])

    return pretty_dictonary
