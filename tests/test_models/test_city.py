#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for the `City` class."""

    def setUp(self):
        """Creates instances before each test."""
        self.c1 = City()
        self.c2 = City(**self.c1.to_dict())
        self.c3 = City("hello", "wait", "in")

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""
        k = f"{type(self.c1).__name__}.{self.c1.id}"
        self.assertIsInstance(self.c1.name, str)
        self.assertEqual(self.c3.name, "")
        self.c1.name = "Abuja"
        self.assertEqual(self.c1.name, "Abuja")

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(self.c1.id, str)
        self.assertIsInstance(self.c1.created_at, datetime)
        self.assertIsInstance(self.c1.updated_at, datetime)
        self.assertEqual(self.c1.updated_at, self.c2.updated_at)

    def test_save(self):
        """Test method for save"""
        old_update = self.c1.updated_at
        self.c1.save()
        self.assertNotEqual(self.c1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        a_dict = self.c2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(self.c2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(self.c1, self.c2)


if __name__ == "__main__":
    unittest.main()
