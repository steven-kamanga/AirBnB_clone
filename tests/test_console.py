#!/usr/bin/python3
"""
Console Tests Module
"""
import unittest
import console
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import pycodestyle


class TestConsole(unittest.TestCase):
    """Class for testing the console module"""
    def test_console_conformity_pycode(self):
        """Tests console.py's adherence to pycodestyle."""
        pycode = pycodestyle.StyleGuide(quiet=True)
        res = pycode.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Tests existence of console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_help(self):
        """Tests help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(s, f.getvalue())

    def test_help_EOF(self):
        """Tests the help EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        s = 'Exits program at EOF\n'
        self.assertEqual(s, f.getvalue())

    def test_help_quit(self):
        """Tests the help quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'QUIT command that exits the program\n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the help create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates a new instance of a class\n'
        self.assertEqual(s, f.getvalue())

    def test_help_show(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        s = 'Prints the string representation of an instance\n'
        self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """Tests the help destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = 'Deletes an instance based on the class name and id\n'
        self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """Tests the help all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        s = 'Prints all string representation of all instances\n'
        self.assertEqual(s, f.getvalue())

    def test_help_count(self):
        """Tests the help count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        s = 'Retrieves the number of instances of a class\n\
        Usage: <class name>.count()\n'
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests the help update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        s = 'Updates an instance based on the class name and id\n'
        self.assertEqual(s, f.getvalue())

    def test_do_EOF(self):
        """Tests the do_EOF method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertTrue(len(f.getvalue()) == 1)
        self.assertEqual("\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF someStuff")
        self.assertTrue(len(f.getvalue()) == 1)
        self.assertEqual("\n", f.getvalue())

    def test_do_quit(self):
        """Tests the do_quit method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        return_val = f.getvalue()
        self.assertEqual("", return_val)
        self.assertTrue(len(return_val) == 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit someStuff")
        self.assertEqual("", f.getvalue())
        self.assertTrue(len(f.getvalue()) == 0)

    def test_emptyline(self):
        """Tests the emptyline method."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual("", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("  \n")
        self.assertEqual("", f.getvalue())


if __name__ == "__main__":
    unittest.main()
