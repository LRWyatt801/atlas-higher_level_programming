#!/usr/bin/python3
"""Module containing text)indentation function"""


def text_indentation(text):
    """Function that prints new line after '.' ':' and '?'

    Args:
        text (str): string of text

    Raises:
        TypeError: wrong type, must be str
    """
    if not isinstance(text, str):  # check text type is str
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
