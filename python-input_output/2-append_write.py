#!/usr/bin/python3
"""Contains append_write function"""


def append_write(filename="", text="") -> int:
    """Appends text to end of filename

    Args:
        filename (str, optional): file to add to. Defaults to "".
        text (str, optional): text to add. Defaults to "".

    Returns:
        int: Number of characters appened
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
