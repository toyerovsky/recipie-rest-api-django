from django.test import TestCase

from .calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Tests that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)
