import unittest
from typing import List

def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    ans = duration
    for i in range(1, len(timeSeries)):
        ans += min(duration, timeSeries[i] - timeSeries[i-1])

    return ans

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findPoisonedDuration([1, 4], 2), 4)

    def test_case_2(self):
        self.assertEqual(findPoisonedDuration([1, 2], 2), 3)
    
    def test_case_3(self):
        self.assertEqual(findPoisonedDuration([1, 2, 3], 2), 4)

if __name__ == '__main__':
    unittest.main()