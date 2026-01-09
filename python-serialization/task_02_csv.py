#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save it to data.json.
    Returns True if successful, False otherwise.
    """
    try:
        data = []

        with open(csv_filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except (FileNotFoundError, PermissionError, OSError):
        return False
