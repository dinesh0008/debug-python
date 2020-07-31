from person import Person
import unittest
from unittest import mock

class SimpleTest(unittest.TestCase):
    @mock.patch("person.get_name", return_value="Bob")
    def test_name(self, _name):
        person = Person()
        name = person.name()
        assert name == "Bob"
