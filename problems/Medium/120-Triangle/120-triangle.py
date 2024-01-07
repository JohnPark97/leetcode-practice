import unittest
from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    # Start from the second last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update each element to be the sum of itself and the min of its two children
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

    # The top element now contains the minimum path sum
    return triangle[0][0]

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11)

    def test_case_2(self):
        self.assertEqual(minimumTotal([[-10]]), -10)
    
    def test_case_3(self):
        self.assertEqual(minimumTotal([[1], [2, 3]]), 3)

if __name__ == '__main__':
    unittest.main()