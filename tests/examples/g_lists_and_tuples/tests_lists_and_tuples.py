import unittest

from src.examples.g_lists_and_tuples.lists import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    
    def test_list_index(self):
        even_numbers = [2,4,6,8,10]
        self.assertEqual(even_numbers[0], 2)
        self.assertEqual(even_numbers[2], 6)

    def test_list_index_strings(self):
        prog_lang = ['Java', 'C++', 'C#', 'Python']
        self.assertEqual(prog_lang[1], 'C++')
        self.assertEqual(prog_lang[3], 'Python')

    def test_list_dif_data_types(self):
        my_addresss = [123, 'Main Street', 78666, True, 50.99, [1,2,3]]
        self.assertEqual(my_addresss[1], 'Main Street')

    def test_create_list_w_range(self):
        nums = list(range(5))
        expected_list = [0,1,2,3,4]
        self.assertEqual(nums, expected_list)