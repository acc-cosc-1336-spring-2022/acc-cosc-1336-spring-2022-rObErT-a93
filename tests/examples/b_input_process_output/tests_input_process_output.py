import unittest

from src.examples.b_input_proc_output.input_process_output import test_config
from src.examples.b_input_proc_output.input_process_output import add_numbers

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    
    def test_add_numbers_1(self):
        self.assertEqual(10, add_numbers(5, 5))

    def test_add_numbers_2(self):
        self.assertEqual(11, add_numbers(5, 6))