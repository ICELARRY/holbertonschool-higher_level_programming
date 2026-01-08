#!/usr/bin/python3
"""Append a string to a UTF-8 text file and return the number of characters."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(
        filename,
        "a",
        encoding="utf-8"
    ) as file:
        return file.write(text)
