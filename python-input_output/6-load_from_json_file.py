#!/usr/bin/python3
"""Create an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Load and return the object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
