#!/usr/bin/python3
"""
Tests for the City model
"""


import unittest
import datetime

from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """Test the city model"""

    def setUp(self):
        """Instances for testing"""
        self.c1 = City()
        self.c2 = City()

    def test_instances(self):
        """Check the instances and presence of attributes"""
        self.assertIsInstance(self.c1, City)
        self.assertIsInstance(self.c2, City)
        self.assertTrue(hasattr(self.c1, "name"))
        self.assertTrue(hasattr(self.c1, "state_id"))

    def test_name(self):
        """Test the name attribute"""
        self.assertEqual(type(self.c1.name), str)
        self.assertEqual(self.c1.name, "")
        self.assertNotEqual(self.c1.name, None)

    def test_state_id(self):
        """Test the state_id attribute"""
        self.assertNotEqual(self.c1.state_id, None)
        self.assertEqual(type(self.c1.state_id), str)
        # self.assertEqual(self.c1.state_id, State.id)
        self.assertEqual(self.c1.state_id, "")


if __name__ == '__main__':
    unittest.main()
