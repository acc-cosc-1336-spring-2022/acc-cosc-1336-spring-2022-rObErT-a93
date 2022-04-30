import unittest #

from src.homework.i_dictionaries_sets.dictionary import add_inventory, get_p_distance, get_p_distance_matrix, remove_inventory_widget

class Test_config(unittest.TestCase):
    
# HW 7
    def test_add_inventory(self):
        inventory_dictionary = {}
        widget_name = 'widget1'
        quantity = 10
        expected_dictionary = {widget_name : quantity}
        self.assertEqual(expected_dictionary, add_inventory(inventory_dictionary, widget_name, quantity))

        inventory_dictionary = {'widget1' : quantity}
        quantity = 25
        expected_dictionary = {'widget1' : 35}
        self.assertEqual(expected_dictionary, add_inventory(inventory_dictionary, widget_name, quantity))

        inventory_dictionary = {'widget1' : 35}
        quantity = -10
        expected_dictionary = {'widget1' : 25}
        self.assertEqual(expected_dictionary, add_inventory(inventory_dictionary, widget_name, quantity))

    def test_remove_inventory_widget(self):
        inventory_dictionary = {}
        widget_name = 'widget1'
        inventory_dictionary['widget1'] = 11
        inventory_dictionary['widget2'] = 24
        expected_dictionary = {'widget2' : 24}
        self.assertEqual(1, len(expected_dictionary))
        self.assertEqual(expected_dictionary, remove_inventory_widget(inventory_dictionary, widget_name))

# HW 6
    def test_get_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertEqual(0.4, get_p_distance(list1, list2))

    def test_get_p_distance_matrix(self):
        list1 = [ ['T','T','T','C','C','A','T','T','T','A'],
                    ['G','A','T','T','C','A','T','T','T','C'],
                    ['T','T','T','C','C','A','T','T','T','T'],
                    ['G','T','T','C','C','A','T','T','T','A']   ]
        
        p_distance_matrix = [   [0.0, 0.4, 0.1, 0.1],
                                [0.4, 0.0, 0.4, 0.3],
                                [0.1, 0.4, 0.0, 0.2],
                                [0.1, 0.3, 0.2, 0.0]    ]
        self.assertEqual(p_distance_matrix, get_p_distance_matrix(list1))
