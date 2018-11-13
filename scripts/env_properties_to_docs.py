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

with open("docs/api_refrence/environment_base.md", "r") as file:
    base_document = file.read()

table = ""
table = table + "| Name | Unit | Help message |" + "\n"
table = table + "| :- | :- | :- |" + "\n"

for _key, property_ in thea.ENV_PROPERTIES.items():

    if property_.long_unit != "" and property_.short_unit != "":
        unit_entry = f"{property_.long_unit} ({property_.short_unit})"
    else:
        unit_entry = ""

    property_entry = (
        f"| {property_.name} | {unit_entry} | {property_.help_.replace('.','')} |"
    )
    table = table + property_entry + "\n"

output_document = base_document.replace("REPLACE_THIS_WITH_TABLE", table)

with open("docs/api_refrence/environment.md", "w") as file:
    file.write(output_document)
