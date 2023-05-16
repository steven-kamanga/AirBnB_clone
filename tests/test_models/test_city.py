#!/usr/bin/python3
"""
Tests the City model
"""


import unittest
import datetime

from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """Test the model"""

    def setUp(self):
        """Instances for testing"""
        self.c1 = City()
        self.c2 = City()

    def test_instances(self):
        self.assertIsInstance(self.c1, City)
        self.assertIsInstance(self.c2, City)
        self.assertTrue(hasattr(self.c1, "name"))
        self.assertTrue(hasattr(self.c1, "state_id"))

    def test_name(self):
        self.assertEqual(type(self.c1.name), str)
        self.assertEqual(self.c1.name, "")
        self.assertNotEqual(self.c1.name, None)

    def test_state_id(self):
        self.assertNotEqual(self.c1.state_id, None)
        self.assertEqual(type(self.c1.state_id), str)
        # self.assertEqual(self.c1.state_id, State.id)
        self.assertEqual(self.c1.state_id, "")


if __name__ == '__main__':
    unittest.main()
