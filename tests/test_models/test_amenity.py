#!/usr/bin/python3
"""
Tests for the Amenity model
"""


import unittest
import datetime

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity Module"""

    def setUp(self):
        """Instance tests and stuff"""
        self.a1 = Amenity()
        self.a2 = Amenity()

    def test_instances(self):
        """Instance tests"""
        self.assertTrue(isinstance(self.a1, Amenity))
        self.assertTrue(isinstance(self.a2, Amenity))
        self.assertTrue(hasattr(self.a1, "name"))

    def test_name(self):
        """test the name"""
        self.assertEqual(type(self.a1.name), str)
        self.assertEqual(self.a1.name, "")
        self.assertNotEqual(self.a1.name, None)


if __name__ == '__main__':
    unittest.main()
