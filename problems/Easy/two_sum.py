import unittest
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    map = {}
    for index, num in enumerate(nums):
        map[num] = index

    for index, num in enumerate(nums):
        target_index = map.get(target - num)
        if target_index and target_index != index:
            return [index, target_index]
        

class TwoSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(two_sum([2, 11, 7, 15], 9), [0, 2])

    def test_case_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_case_3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_case_4(self):
        self.assertEqual(two_sum([-3, 0, 3, 31], 0), [0, 2])
    
if __name__ == '__main__':
    unittest.main()