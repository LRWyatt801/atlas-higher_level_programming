#!/usr/bin/python3
"""Contains read_file function"""


def read_file(filename="") -> None:
    """Prints an input file to stdout

    Args:
        filename (str, optional): text file. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
