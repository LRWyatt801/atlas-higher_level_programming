#!/usr/bin/python3
"""unittest file for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([...])"""
    
    def test_ordered_list(self):
        """test for ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """test for unordered list"""
        unordered = [2, 4, 1 , 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beggining(self):
        """test for max at beggining list"""
        beggining = [4, 3, 2, 1]
        self.assertEqual(max_integer(beggining), 4)

    def test_max_neg_num(self):
        """test with neg num"""
        neg = [-1, 2, 3, 4]
        self.assertEqual(max_integer(neg), 4)

    def test_only_neg_num(self):
        """test with only neg numbers"""
        onlyneg = [-1, -2, -3, -4]
        self.assertEqual(max_integer(onlyneg), -1)

    def test_one_element(self):
        """"test list with one element"""
        onlyone = [1]
        self.assertEqual(max_integer(onlyone), 1)

    def test_empty_list(self):
        """test empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)