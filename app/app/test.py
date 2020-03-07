from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):
    def test_add_number(self):
        """test add"""
        self.assertEqual(add(3, 11), 14)

    def test_subtract_numbers(self):
        """test substac """
        self.assertEqual(subtract(5, 11), 6)
