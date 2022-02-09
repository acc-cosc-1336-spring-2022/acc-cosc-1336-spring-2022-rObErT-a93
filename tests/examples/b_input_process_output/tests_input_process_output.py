import unittest

    #documents what I've been testing
from src.examples.b_input_proc_output.input_process_output import exponentiate_me, get_remainder, test_config
from src.examples.b_input_proc_output.input_process_output import add_numbers
from src.examples.b_input_proc_output.input_process_output import multiply_numbers
from src.examples.b_input_proc_output.input_process_output import integer_division
from src.examples.b_input_proc_output.input_process_output import float_division
from src.examples.b_input_proc_output.input_process_output import operator_precedence_1
from src.examples.b_input_proc_output.input_process_output import operator_precedence_2
from src.examples.b_input_proc_output.input_process_output import exponentiate_me
from src.examples.b_input_proc_output.input_process_output import get_remainder

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    
    def test_add_numbers_1(self):
        self.assertEqual(10, add_numbers(5, 5)) #assertion

    def test_add_numbers_2(self):
        self.assertEqual(11, add_numbers(5, 6)) #assertion

    def test_multiply_numbers_w_out_params(self):
        self.assertEqual(25, multiply_numbers(5, 5))

    def test_interger_division_1(self):
        self.assertEqual(3, integer_division(6, 2)) #assertion

    def test_float_division(self):
        self.assertEqual(2.5, float_division(5, 2)) #assertion

    def test_operator_precedence_1(self): #12+6/3
        self.assertEqual(14, operator_precedence_1(12, 6, 3))

    def test_operator_precedence_2(self): #(12+6)/3
        self.assertEqual(6, operator_precedence_2(12, 6, 3)) #assertion
    
    def test_exponentiate_me(self):
        self.assertEqual(256, exponentiate_me(2, 8))
        self.assertEqual(128, exponentiate_me(2, 7))
        self.assertEqual(64, exponentiate_me(2, 6))
        self.assertEqual(32, exponentiate_me(2, 5))
        self.assertEqual(16, exponentiate_me(2, 4))
    
    def test_get_remainder(self):
        self.assertEqual(1, get_remainder(5, 2))