#!/usr/bin/python3
"""Write a string to a UTF-8 text file and return the number of characters."""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        return file.write(text)
