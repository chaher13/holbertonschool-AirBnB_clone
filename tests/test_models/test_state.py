#!/usr/bin/python3
"""
This module provides testing for the State class.
"""
from models.base_model import BaseModel
from models.state import State
import unittest
import datetime
import models
import os


class TestState(unittest.TestCase):
    """
    Test the State class
    """

    dico = models.storage.all().copy()
    for k, v in dico.items():
        del models.storage.all()[k]
    models.storage.save()
    var = State()

    def test_state_id(self):
        """Test the type of id"""
        self.assertIsInstance(TestState.var.id, str)

    def test_state_created_at(self):
        """Test the type of created_at"""
        self.assertIsInstance(TestState.var.created_at, datetime.datetime)

    def test_state_updated_at(self):
        """test the type of updated_at"""
        self.assertIsInstance(TestState.var.updated_at, datetime.datetime)

    def test_base_case(self):
        """Base case: instantiation of the class State"""
        self.assertEqual(type(TestState.var), State)

    def test_state_name(self):
        """test the type of the name"""
        self.assertIsInstance(TestState.var.name, str)

    def test_add_attr(self):
        """Test adding a new attribute"""
        u1 = State()
        u1.color = "green"
        dico_state = u1.to_dict()
        u1.save()
        self.assertEqual(u1.color, "green")
        self.assertIsInstance(u1, State)
        self.assertEqual(type(dico_state), dict)

    def test_update_add(self):
        """Test updating attributes"""
        u2 = State()
        u2.name = "Paris"
        self.assertEqual(u2.name, "Paris")
        self.assertIsInstance(u2, State)
        u3 = State()
        self.assertLess(u2.created_at, u3.created_at)
        self.assertLess(u2.updated_at, u3.updated_at)


if __name__ == '__main__':
    unittest.main()
