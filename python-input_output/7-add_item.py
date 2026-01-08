#!/usr/bin/python3
"""
7-add_item.py
Adds all command-line arguments to a list and saves them to a JSON file.
"""

import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

# Load existing list from file, or start with an empty list if file doesn't exist
if Path(file_name).is_file():
    items = load_from_json_file(file_name)
else:
    items = []

# Add all command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, file_name)

