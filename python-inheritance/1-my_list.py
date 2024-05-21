#!/usr/bin/python3
"""Module contaning a class"""


class MyList(list):
    """subclass of list

    Args:
        list (class): parent class
    """
    def print_sorted(self):
        ordered = self[:]
        ordered.sort()
        print(ordered)
