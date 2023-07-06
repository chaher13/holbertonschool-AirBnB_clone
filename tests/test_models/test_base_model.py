#!/usr/bin/python3
"""
This module providees testing for the BasModel class.
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_arg(self):
        """
        Test the instantiation of BaseModel with no arguments.
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(hasattr(b1, "id"))
        self.assertIsInstance(b1.id, str)


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Create an instance of BaseModel"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clear the instance after each test"""
        self.base_model = None

    def test_attributes(self):
        """Test if the instance has the expected attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        """Test if the id attribute is generated as expected"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_and_updated_at(self):
        """Test if created_at and updated_at attributes are datetime objects"""
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test if __str__ method returns the expected string representation"""
        expected = \
            f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns the expected dictionary"""
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
