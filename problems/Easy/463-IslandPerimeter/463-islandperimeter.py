from typing import List
import unittest

def islandPerimeter(grid: List[List[int]]) -> int:
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                ans += check_adjacents(grid, i, j)
    return ans


def check_adjacents(grid: List[List[int]], i: int, j: int, sides = 4) -> int:
    # left
    left = j - 1

    # right
    right = j + 1

    # up
    up = i - 1

    # down
    down = i + 1

    ans = 0
    if left < 0:
        #  or grid[left][j] == 0:
        ans += 1
    elif grid[i][left] == 0:
        ans += 1

    if right >= len(grid[0]):
    #  or grid[right][j] == 0:
        ans += 1
    elif grid[i][right] == 0:
        ans += 1
    if up < 0:
        #  or grid[i][up] == 0:
        ans += 1
    elif grid[up][j] == 0:
        ans += 1
    if down >= len(grid):
        #  or grid[i][down] == 0:
        ans += 1
    elif grid[down][j] == 0:
        ans += 1

    return ans


class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(islandPerimeter([[0, 1, 0, 0],
                                          [1, 1, 1, 0],
                                          [0, 1, 0, 0],
                                          [1, 1, 0, 0]]), 16)
        
    def test_case_2(self):
        self.assertEqual(islandPerimeter([[1]]), 4)

    def test_case_3(self):
        self.assertEqual(islandPerimeter([[1, 0]]), 4)

if __name__ == '__main__':
    unittest.main()