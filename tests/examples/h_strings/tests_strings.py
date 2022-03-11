import unittest

from src.examples.h_strings.strings import concat_strings, slice_str, string_sub_string, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    
    def test_concat_strings(self):
        self.assertEqual('john doe', concat_strings('john ', 'doe'))
    
    def test_slice_strings(self):
        self.assertEqual('Lynn', slice_str('Patty Lynn Smith'))
    
    def test_sub_strings(self):
        str = 'Four score and seven years ago'
        sub_string = 'seven'
        self.assertEqual(True, string_sub_string(str, sub_string))
        self.assertNotEqual(True, string_sub_string(str, 'eight'))

    def test_string_repetition(self):       # 3/10/2022 Lecture
        str = 'w' * 5
        self.assertEqual(str, 'wwwww')