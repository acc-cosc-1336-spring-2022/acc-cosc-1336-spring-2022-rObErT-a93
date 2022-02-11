import unittest
from webbrowser import get

from src.examples.c_decisions.decisions import get_letter_grade, is_even, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_not_truth_table(self):
        self.assertEqual(not True, False)
        self.assertEqual(not False, True)

    def test_and_truth_table(self):
        self.assertEqual(True and True, True)
        self.assertEqual(True and False, False)
        self.assertEqual(False and True, False)
        self.assertEqual(False and False, False)

    def test_or_truth_table(self):
        self.assertEqual(True or True, True)
        self.assertEqual(True or False, True)
        self.assertEqual(False or True, True)
        self.assertEqual(False or False, False)

    def test_is_even(self):
        self.assertEqual(True, is_even(4))

    def test_character_comparison(self):
        self.assertEqual('a' == 'A', False)
        self.assertEqual('a' > 'A', True)

    def test_get_letter_grade(self):
        self.assertEqual('A', get_letter_grade(90))
        self.assertEqual('B', get_letter_grade(85))
        self.assertEqual('C', get_letter_grade(74))
        self.assertEqual('D', get_letter_grade(63))
        self.assertEqual('F', get_letter_grade(54))