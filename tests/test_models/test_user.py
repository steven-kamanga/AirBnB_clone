#!/usr/bin/python3
"""
Tests for the User Model
"""


import unittest
import datetime

from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for the User Model
    1. Check for attributes
    2. Check for methods
    3. Check Expected output
    4. Check Empty strings
    """

    def setUp(self):
        """Let's create a few instances to test with"""
        self.u1 = User()
        self.u2 = User()

    def test_instances(self):
        """Test if instances are created"""
        self.assertTrue(isinstance(self.u1, User))
        self.assertTrue(isinstance(self.u2, User))
        self.assertTrue(hasattr(self.u1, "email"))
        self.assertTrue(hasattr(self.u1, "password"))
        self.assertTrue(hasattr(self.u1, "first_name"))
        self.assertTrue(hasattr(self.u1, "last_name"))

    def test_email(self):
        """Tests the email attribute"""
        self.assertEqual(type(self.u1.email), str)
        self.assertEqual(self.u1.email, "")
        self.assertNotEqual(self.u1.email, None)

    def test_password(self):
        """Tests the password attribute"""
        self.assertEqual(type(self.u1.password), str)
        self.assertEqual(self.u1.password, "")
        self.assertNotEqual(self.u1.password, None)

    def test_first_name(self):
        """Tests the first_name attribute"""
        self.assertEqual(type(self.u1.first_name), str)
        self.assertEqual(self.u1.first_name, "")
        self.assertNotEqual(self.u1.first_name, None)

    def test_last_name(self):
        """Tests the last_name attribute"""
        self.assertEqual(type(self.u1.last_name), str)
        self.assertEqual(self.u1.last_name, "")
        self.assertNotEqual(self.u1.last_name, None)


if __name__ == '__main__':
    unittest.main()
