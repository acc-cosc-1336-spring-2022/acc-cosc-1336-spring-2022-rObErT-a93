import unittest
from src.homework.c_decisions.decisions import get_faculty_rating, get_options_ratio

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        self.assertEqual(.25, get_options_ratio(5, 20))
        self.assertEqual(.5, get_options_ratio(10, 20))

    def test_get_faculty_rating(self):
        self.assertEqual('Excellent', get_faculty_rating(get_options_ratio(9.1,10)))
        self.assertEqual('Very Good', get_faculty_rating(get_options_ratio(8.5, 10)))
        self.assertEqual('Good', get_faculty_rating(get_options_ratio(7.1, 10)))
        self.assertEqual('Needs Improvement', get_faculty_rating(get_options_ratio(6.6, 10)))
        self.assertEqual('Unacceptable', get_faculty_rating(get_options_ratio(5.9, 10)))
        self.assertEqual('Unacceptable', get_faculty_rating(get_options_ratio(4.5, 10)))