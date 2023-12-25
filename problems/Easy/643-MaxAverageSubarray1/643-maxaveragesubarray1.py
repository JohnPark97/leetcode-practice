import unittest
from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    ptr1 = 0
    ptr2 = 0

    # first use the ptr2 to iterate by k and get the first average
    # if len(nums) is 4 and k is 2, then ptr2 should go up to 1
    prev_sum = 0
    while ptr2 < k:
        prev_sum += nums[ptr2] 
        ptr2 += 1

    max_sum = prev_sum
    while ptr2 < len(nums):
        prev_sum = prev_sum - nums[ptr1] + nums[ptr2]
        max_sum = max(max_sum, prev_sum)
        # minus the previous max_sum by ptr1 value but add ptr2 value after incrementing them by 1
        ptr1 += 1
        ptr2 += 1

    return max(prev_sum, max_sum) / k
    

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)

    def test_case_2(self):
        self.assertEqual(findMaxAverage([-1], 1), -1)

    def test_case_3(self):
        self.assertEqual(findMaxAverage([4,2,1,3,3], 2), 3)

if __name__ == '__main__':
    unittest.main()