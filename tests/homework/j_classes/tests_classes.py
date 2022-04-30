import unittest
from src.homework.j_classes import class_a

class Test_Config(unittest.TestCase):

    def test_roll_value(self):
        die = class_a.Die()
        die.roll()
        if die.get_roll_value() in range(0,7):
            rolled = True
        else:
            rolled = False
        self.assertEqual(True,rolled)

    def test_first_roll(self):
        die = class_a.Die()
        die.roll()
        self.assertEqual(True, die.get_roll_value() in range(0,7))

    def test_second_roll(self):
        die = class_a.Die()
        die.roll()
        self.assertEqual(True, die.get_roll_value() in range(0,7))

    def test_third_roll(self):
        die = class_a.Die()
        die.roll()
        self.assertEqual(True, die.get_roll_value() in range(0,7))

    def test_roll_outside_range(self):
        die = class_a.Die()
        die.roll()
        self.assertEqual(False, die.get_roll_value() in range(7,13))