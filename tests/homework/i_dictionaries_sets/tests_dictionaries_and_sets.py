import unittest #

from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix

class Test_config(unittest.TestCase):

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
