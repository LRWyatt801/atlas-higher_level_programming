#!/usr/bin/python3
"""Contains write_file function"""


def write_file(filename="", text="") -> int:
    """writes a string to a text file

    Args:
        filename (str, optional): filename of text file. Defaults to "".
        text (str, optional): string to write. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
