#!/usr/bin/python3
"""
This module provides testing for the Amenity class.
"""

from models.base_model import BaseModel
import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""
    def test_type_amenity_id(self):
        """Test the type of the id attribute."""
        var = Amenity()
        self.assertIsInstance(var.id, str)

    def test_type_amenity_created_at(self):
        """Test the type of the created_at attribute."""
        var = Amenity()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_type_amenity_updated_at(self):
        """Test the type of the updated_at attribute."""
        var = Amenity()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    def test_type_amenity_name(self):
        """Test the type of the name attribute."""
        var = Amenity()
        self.assertIsInstance(var.id, str)

    def test_amenity_name_initial_value(self):
        """Test the initial value of the name attribute."""
        var = Amenity()
        self.assertEqual(var.name, "")

    def test_amenity_name_assignment(self):
        """Test the assignment of a value to the name attribute."""
        var = Amenity()
        var.name = "Gym"
        self.assertEqual(var.name, "Gym")

    def test_amenity_to_dict(self):
        """Test the to_dict method of the Amenity class."""
        var = Amenity()
        amenity_dict = var.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test_amenity_str_representation(self):
        """Test the string representation of the Amenity object."""
        var = Amenity()
        expected_string = "[Amenity] ({}) {}".format(var.id, var.__dict__)
        self.assertEqual(str(var), expected_string)

    def test_amenity_custom_attributes(self):
        """Test the addition of custom attributes to the Amenity object."""
        var = Amenity()
        var.custom_attr = "Custom Value"
        self.assertEqual(var.custom_attr, "Custom Value")


if __name__ == '__main__':
    unittest.main()
