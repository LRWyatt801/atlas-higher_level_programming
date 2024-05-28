#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    
    def setUp(self) -> None:
        # Reset the id counter before each test
        Base._id_counter = 1

    def test_auto_id_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_manual_id_assignment(self):
        b1 = Base(42)
        b2 = Base(1)
        self.assertEqual(b1.id, 42)
        self.assertEqual(b2.id, 1)

    def test_various_input(self):
        b1 = Base(42)
        b2 = Base()
        b3 = Base()
        b4 = Base(4)
        self.assertEqual(b1.id, 42)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 4)


if __name__ == '__main__':
    unittest.main()