import unittest
from typing import List

class MyTest(unittest.TestCase):
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()

        highest = nums[len(nums) - 1]

        counter = 0
        acc = 0 # this is to keep track of all the subtractions
        for i in range(len(nums)):
            diff = nums[i] - acc
            if diff > 0:
                highest -= diff
                acc += diff
                counter += 1
            if highest <= 0:
                return counter

        return 0
    
    def test_case_1(self):
        self.assertEqual(self.minimumOperations([1, 1, 1]), 1)

    def test_case_2(self):
        self.assertEqual(self.minimumOperations([0]), 0)

    def test_case_3(self):
        self.assertEqual(self.minimumOperations([3, 2, 1]), 3)

    def test_case_4(self):
        self.assertEqual(self.minimumOperations([1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()