import unittest
from typing import List
import sys
import os

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'problems'))

from problems.merge_sorted_array import MergeSortedArray


class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.mergeSortedArray = MergeSortedArray()
    
    def test_basic_merge(self):
        """Test basic merge functionality"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])
    
    def test_empty_nums2(self):
        """Test when nums2 is empty"""
        nums1 = [1, 2, 3]
        m = 3
        nums2 = []
        n = 0
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])
    
    def test_empty_nums1(self):
        """Test when nums1 only contains zeros (effectively empty)"""
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])
    
    def test_all_nums2_smaller(self):
        """Test when all elements in nums2 are smaller than nums1"""
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])
    
    def test_all_nums2_larger(self):
        """Test when all elements in nums2 are larger than nums1"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [4, 5, 6]
        n = 3
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])
    
    def test_interleaved_merge(self):
        """Test when elements need to be interleaved"""
        nums1 = [1, 3, 5, 0, 0, 0]
        m = 3
        nums2 = [2, 4, 6]
        n = 3
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])
    
    def test_duplicate_elements(self):
        """Test with duplicate elements"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 2, 3]
        n = 3
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 2, 3, 3])
    
    def test_single_elements(self):
        """Test with single elements in each array"""
        nums1 = [2, 0]
        m = 1
        nums2 = [1]
        n = 1
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2])
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums1 = [-3, -1, 0, 0, 0]
        m = 2
        nums2 = [-2, 0, 1]
        n = 3
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [-3, -2, -1, 0, 1])
    
    def test_larger_array(self):
        """Test with larger arrays"""
        nums1 = [1, 3, 5, 7, 9, 0, 0, 0, 0]
        m = 5
        nums2 = [2, 4, 6, 8]
        n = 4
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_unequal_array_sizes(self):
        """Test with arrays of different sizes"""
        nums1 = [1, 0, 0, 0, 0]
        m = 1
        nums2 = [2, 3, 4, 5]
        n = 4
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])
    
    def test_leetcode_example_1(self):
        """Test LeetCode Example 1"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])
    
    def test_leetcode_example_2(self):
        """Test LeetCode Example 2"""
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])
    
    def test_leetcode_example_3(self):
        """Test LeetCode Example 3"""
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        
        self.mergeSortedArray.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])


if __name__ == '__main__':
    unittest.main()