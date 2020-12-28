import unittest
import sys
import os

def fix_path():
    # VS code bug: https://github.com/microsoft/vscode-python/issues/8678
    # p = os.getcwd()[:-4]
    sys.path.append('/Users/randyclinton/sideprojects/grokking-algs-exercises/ch1/binary_search/python/')
fix_path()
import search


sorted_list = [0,1,2,3,4,5]
class TestCase(unittest.TestCase):

    def test_find_middle_event(self):
        ix = search.find_middle( [ 1,2,3,4] )
        self.assertEquals(ix, 2)

    def test_find_middle_odd(self):
        ix = search.find_middle( [ 1,2,3] )
        self.assertEquals(ix, 1)    
    
    def test_find_value_simple(self):
        print("found test")
        ix = search.binary_search( [1,2,3], 2)

        self.assertEqual(ix, 1)

    def test_find_value_top_half(self):
        print("found test")
        ix = search.binary_search( sorted_list, 1)

        self.assertEqual(ix, 5)
    
    def test_find_value_bottom_half(self):
        print("found test")
        ix = search.binary_search( sorted_list, 4)

        self.assertEqual(ix, 5)
    

    def test_handle_no_value(self):

        ix = search.binary_search( sorted_list, -1)

        self.assertIsNone(ix)