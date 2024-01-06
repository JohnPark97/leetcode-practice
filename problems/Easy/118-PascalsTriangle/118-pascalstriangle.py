import unittest
from typing import List

def generate(numRows: int) -> List[List[int]]:

    ans = [[1]]
    for i in range(1, numRows):
        row = [1] * (i + 1)
        for j in range(i):
            if j < i and j > 0:
                row[j] = ans[i-1][j-1] + ans[i-1][j]
        ans.append(row)

    return ans

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(generate(1), [[1]])

    def test_case_2(self):
        self.assertEqual(generate(2), [[1], [1, 1]])
    
    def test_case_3(self):
        self.assertEqual(generate(3), [[1], [1, 1], [1, 2, 1]])
    
    def test_case_4(self):
        self.assertEqual(generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        

if __name__ == '__main__':
    unittest.main()