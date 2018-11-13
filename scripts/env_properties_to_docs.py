"""A script used to generate documentation on the environment properties.

This script takes the file environment_base.md as input and replaces
the string REPLACE_THIS_WITH_TABLE with a table of environment properties.
The combined file is saves as environment.md"""

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# flake8: noqa E402
import thea

REPLACE_KEY = "REPLACE_THIS_WITH_TABLE"
BASE_FILE = "docs/api_refrence/environment_base.md"
TARGET_FILE = "docs/api_refrence/environment.md"

def main():

    with open(BASE_FILE, "r", encoding='utf8') as file:
        base_document = file.read()

    print(f'Opened: "{BASE_FILE}"')

    table = ""
    table = table + "| Name | Key | Unit | Help message |" + "\n"
    table = table + "| :- | :- | :- | :- |" + "\n"

    for key, property_ in sorted(thea.ENV_PROPERTIES.items()):

        if property_.long_unit != "" and property_.short_unit != "":
            unit_entry = f"{property_.long_unit} ({property_.short_unit})"
        else:
            unit_entry = ""

        property_entry = (
            f"| {property_.name} | `'{key}'` | {unit_entry} | {property_.help_.replace('.','')} |"
        )
        table = table + property_entry + "\n"

    output_document = base_document.replace(REPLACE_KEY, table)

    with open(TARGET_FILE, "w", encoding='utf8') as file:
        file.write(output_document)

    print(f'Saved: "{TARGET_FILE}"')

if __name__ == "__main__":
    main()
