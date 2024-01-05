import unittest
from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        max_num1 = m - 1
        total = m + n - 1

        i = n - 1
        while i >= 0:
            if max_num1 < 0:
                nums1[i] = nums2[i]
                i -= 1
            elif nums2[i] >= nums1[max_num1]:
                nums1[total] = nums2[i]
                total -= 1
                i -= 1
            else: # max of num1 is greater than nums2
                nums1[total] = nums1[max_num1]
                max_num1 -= 1
                total -= 1

class MyTest(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        merge(nums1, 3, [2, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_case_2(self):
        nums1 = [1]
        merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])
    
    def test_case_3(self):
        nums1 = [0]
        merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

    def test_case_4(self):
        nums1 = [1, 0]
        merge(nums1, 1, [2], 1)
        self.assertEqual(nums1, [1, 2])

if __name__ == '__main__':
    unittest.main()