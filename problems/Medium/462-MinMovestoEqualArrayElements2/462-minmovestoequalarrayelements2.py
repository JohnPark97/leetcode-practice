import unittest
from typing import List

def minMoves2(nums: List[int]) -> int:
    nums.sort()
    mid = nums[len(nums)//2]

    ans = 0
    for i in range(len(nums)//2):
        ans += abs(mid - nums[i]) + abs(mid - nums[len(nums)-1 - i])

    return ans
    
class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minMoves2([1, 2, 3]), 2)

    def test_case_2(self):
        self.assertEqual(minMoves2([1, 2, 3, 4]), 4)
    
    def test_case_3(self):
        self.assertEqual(minMoves2([1, 2, 3, 4, 5]), 6)

    def test_case_4(self):
        self.assertEqual(minMoves2([1, 2, 3, 4, 5, 6]), 9)

if __name__ == '__main__':
    unittest.main()