#!/usr/bin/python3
"""Defines unittests for console.py.
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Base class for testing Console.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_simple(self):
        """Tests basic commands.
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("?")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? get_all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help get_all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("help destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")


class TestBaseModel(unittest.TestCase):
    """Testing `Basemodel `commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.get_all().keys())

    def test_all_basemodel(self):
        """Test all basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('get_all BaseModel')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "green"
            HBNBCommand().onecmd(f'show BaseModel {b1.id}')
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(f'update BaseModel {b1.id} name "Ife"')
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            HBNBCommand().onecmd(f'update BaseModel {b1.id} age 25')
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.savings = 25.67
            HBNBCommand().onecmd(f'update BaseModel {b1.id} savings 35.89')
            self.assertIn("savings", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'update BaseModel {b1.id} age 10 color "green"'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {bm.id}')
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.get_all().





import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from console import HBNBCommand

class TestUser(unittest.TestCase):
    """Testing the `User` commands.
    """

    def setUp(self):
        pass

    def tearDown(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_all_user(self):
        """Test all user objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(f'show User {us.id}')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(f'update User {us.id} name "Ife"')
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(f'update User {us.id} age 25')
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'update User {us.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_update_user_dict(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            cmmd = f'update User {us.id} {{"age": 25, "color": "black"}}'
            HBNBCommand().onecmd(cmmd)
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy user object."""
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(f'destroy User {us.id}')
            self.assertNotIn("User.{}".format(us.id), storage.all().keys())

class TestUserDotNotation(unittest.TestCase):
    """Testing the `User` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.create()')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_count_user(self):
        """Test count user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
            count = sum(1 for obj in storage.all().values() if type(obj) == User)
            self.assertEqual(int(f.getvalue()), count)

    def test_all_user(self):
        """Test all user objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.all()')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(f'User.show({us.id})')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(f'User.update({us.id}, name, "Ife")')
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(f'User.update({us.id}, age, 25)')
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'User.update({us.id}, age, 10, color, green)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_update_user_dict(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            cmmd = f'User.update({us.id}, {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(cmmd)
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy user object."""
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(f'User.destroy({us.id})')
            self.assertNotIn("User.{}".format(us.id), storage.all().keys())

class TestState(unittest.TestCase):
    """Testing the `State` commands.
    """

    def setUp(self):
        pass

    def tearDown(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_all_state(self):
        """Test all state objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all State')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "green"
            HBNBCommand().onecmd(f'show State {st.id}')
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
         """Test update state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cecilia"
            HBNBCommand().onecmd(f'update State {st.id} name "Ife"')
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBN

def test_all_municipality(self):
    """Test all municipality object.
    """
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd('all Municipality')
        for item in json.loads(f.getvalue()):
            self.assertEqual(item.split()[0], '[Municipality]')

def test_show_municipality(self):
    """Test show municipality object.
    """
    with patch('sys.stdout', new=StringIO()) as f:
        mncplty = Municipality()
        mncplty.eyes = "green"
        HBNBCommand().onecmd(f'show Municipality {mncplty.id}')
        res = f"[{type(mncplty).__name__}] ({mncplty.id}) {mncplty.__dict__}"
        self.assertEqual(f.getvalue().strip(), res)

def test_update_municipality(self):
    """Test update municipality object.
    """
    with patch('sys.stdout', new=StringIO()) as f:
        mncplty = Municipality()
        mncplty.name = "Cecilia"
        HBNBCommand().onecmd(f'update Municipality {mncplty.id} name "Ife"')
        self.assertEqual(mncplty.__dict__["name"], "Ife")

    with patch('sys.stdout', new=StringIO()) as f:
        mncplty = Municipality()
        mncplty.age = 75
        HBNBCommand().onecmd(f'update Municipality {mncplty.id} age 25')
        self.assertIn("age", mncplty.__dict__.keys())
        self.assertEqual(mncplty.__dict__["age"], 25)

    with patch('sys.stdout', new=StringIO()) as f:
        mncplty = Municipality()
        mncplty.age = 60
        cmmd = f'update Municipality {mncplty.id} age 10 color green'
        HBNBCommand().onecmd(cmmd)
        self.assertIn("age", mncplty.__dict__.keys())
        self.assertNotIn("color", mncplty.__dict__.keys())
        self.assertEqual(mncplty.__dict__["age"], 10)

def test_destroy_municipality(self):
    """Test destroy municipality object.
    """
    with patch('sys.stdout', new=StringIO()):
        mncplty = Municipality()
        HBNBCommand().onecmd(f'destroy Municipality {mncplty.id}')
        self.assertNotIn("Municipality.{}".format(
            mncplty.id), storage.all().keys())


class TestMunicipalityDotNotation(unittest.TestCase):
    """Testing the `municipality` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_municipality(self):
        """Test create municipality object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Municipality.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Municipality.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_municipality(self):
        """Test count municipality object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Municipality.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Municipality:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_municipality(self):
        """Test all municipality object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Municipality.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Municipality]')

    def test_show_municipality(self):
        """Test show municipality object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            mncplty = Municipality()
            mncplty.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Municipality.show({mncplty.id})'))
            res = f"[{type(mncplty).__name__}] ({mncplty.id}) {mncplty.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_municipality(self):
        """Test update municipality object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            mncplty = Municipality()
            mncplty.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Municipality.update({mncplty.id}, name, "Ife")'))
            self.assertEqual(mncplty.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            mncplty = Municipality()
            mncplty.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Municipality.update({mncplty.id}, age, 25)'))
            self.assertIn("age", mncplty.__dict__.keys())
            self.assertEqual(mncplty.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            mncplty = Municipality()
            mncplty.age = 60
            cmmd = f'Municipality.update({mncplty.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", mncplty.__dict__.keys())
            self.assertNotIn("color", mncplty.__dict__.keys())
            self.assertEqual(mncplty.__dict__["age"], 10)

    def test_update_municipality_dict(self):
        """Test update municipality object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            mncplty = Municipality()
            mncplty.age = 75
            cmmd = f'Municipality.update({mncplty.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(mncplty.__dict__["age"], 25)
            self.assertIsInstance(mncplty.__dict__["age"], int)

    def test_destroy_municipality(self):
        """Test destroy municipality object.
        """
        with patch('sys.stdout', new=StringIO()):
            mncplty = Municipality()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Municipality.destroy({mncplty.id})'))
            self.assertNotIn("Municipality.{}".format(
                mncplty.id), storage.all().keys())
