import unittest
from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    curr_streak = 0
    max_streak = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            curr_streak += 1
        else:
            max_streak = max(curr_streak, max_streak)
            curr_streak = 0
    max_streak = max(curr_streak, max_streak)

    return max_streak

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)

    def test_case_2(self):
        self.assertEqual(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2)

    def test_case_3(self):
        self.assertEqual(findMaxConsecutiveOnes([0]), 0)

if __name__ == '__main__':
    unittest.main()