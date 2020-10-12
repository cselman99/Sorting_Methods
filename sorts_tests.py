import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection(self):
        nums = [5, 4, 3, 2, 1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [1, 2, 3, 4, 5])
        nums = [3, 2, 1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 3)
        self.assertEqual(nums, [1, 2, 3])

    def test_insertion(self):
        nums = [5, 4, 3, 2, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [1, 2, 3, 4, 5])
        nums = [3, 2, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 3)
        self.assertEqual(nums, [1, 2, 3])
        nums = [1, 2, 3]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 2)

if __name__ == '__main__': 
    unittest.main()
