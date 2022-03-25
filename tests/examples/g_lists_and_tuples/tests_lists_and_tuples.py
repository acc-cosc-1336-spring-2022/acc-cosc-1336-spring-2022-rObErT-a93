import unittest

from src.examples.g_lists_and_tuples.lists import append_item_to_list, find_items_in_lists, test_config

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

    def test_create_list_of_odd_numbers(self):      # 3/22 Lecture
        nums = list(range(1, 10, 2))
        expected_list = [1, 3, 5, 7, 9]
        self.assertEqual = (nums, expected_list)

    def test_create_list_w_repetion_operator(self):
        nums = [0] * 5
        expected_list = [0,0,0,0,0]
        self.assertEqual = (nums, expected_list)

    def test_concat_lists(self):
        list1 = [1,2,3,4]
        list2 = [5,6,7,8]
        list3 = list1 + list2
        expected_list = [1,2,3,4,5,6,7,8]
        self.assertEqual = (list3, expected_list)

    def test_concat_string_lists(self):
        prog_lang = ["C++", "C#"]
        prog_lang += ['Python','Java']      # appending to a list
        expected_list = ["C++", "C#", "Python", "Java"]
        self.assertEqual(prog_lang, expected_list)

    def test_slicing_days(self):
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        expected_list = ['Tuesday','Wednesday','Thursday']
        mid_days = days[2:5]
        self.assertEqual(expected_list, mid_days)

    def test_find_items_in_lists(self):
        list1 = ["C++", "C#", "Python", "Java"]
        self.assertEqual(True, find_items_in_lists('C++', list1))
        self.assertEqual(False, find_items_in_lists('Ada', list1))

    def test_append_item_to_list(self):
        list1 = []
        append_item_to_list('C++', list1)
        append_item_to_list('Python', list1)
        expected_list = ['C++' ,'Python']
        self.assertEqual(expected_list, list1)
