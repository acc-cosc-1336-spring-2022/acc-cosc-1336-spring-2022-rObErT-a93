import unittest

from src.examples.e_functions.value_return_functions import local_variable, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_local_variable(self):
        self.assertEqual(10, local_variable(10))

    def test_local_variable_scope(self):
        val0 = 0
        val = local_variable(val0)
        self.assertEqual(0, val0)
        self.assertEqual(0, val)