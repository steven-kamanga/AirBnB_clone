#!/usr/bin/python3
"""
Tests for the State Model
"""


import unittest
import datetime

from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State model"""

    def setUp(self):
        """Create a few instances for testing"""
        self.s1 = State()

    def test_instances(self):
        """Test if instances are created"""
        self.assertTrue(isinstance(self.s1, State))

    def test_name(self):
        """Test the name attribute"""
        self.assertNotEqual(self.s1.name, None)
        self.assertEqual(type(self.s1.name), str)
        self.assertEqual(self.s1.name, "")


if __name__ == '__main__':
    unittest.main()
