#!/usr/bin/python3
"""Module contaning a class"""


class MyList(list):
    def print_sorted(self):
        ordered = self[:]
        ordered.sort()
        print(ordered)
