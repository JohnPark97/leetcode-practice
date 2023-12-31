import unittest
from typing import List

def find132pattern(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    stack = []
    second = float('-inf')

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < second:
            return True
        while stack and nums[i] > stack[-1]:
            second = stack.pop()
        stack.append(nums[i])

    return False

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find132pattern([1, 2, 3, 4]), False)

    def test_case_2(self):
        self.assertEqual(find132pattern([3, 1, 4, 2]), True)

    def test_case_3(self):
        self.assertEqual(find132pattern([-1, 3, 2, 0]), True)

if __name__ == '__main__':
    unittest.main()