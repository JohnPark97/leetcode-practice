import unittest
from typing import List

def nextGreaterElements(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    ans = [-1] * len_nums
    stack = []

    for i in range(2 * len_nums - 1, -1, -1):
        i = i % len_nums
        # Compare values in nums instead of indices
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            ans[i] = nums[stack[-1]]
        stack.append(i)

    return ans

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(nextGreaterElements([1, 2, 1]), [2, -1, 2])

    def test_case_2(self):
        self.assertEqual(nextGreaterElements([5, 1, 3, 2]), [-1, 3, 5, 5])

    def test_case_3(self):
        self.assertEqual(nextGreaterElements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])

if __name__ == '__main__':
    unittest.main()