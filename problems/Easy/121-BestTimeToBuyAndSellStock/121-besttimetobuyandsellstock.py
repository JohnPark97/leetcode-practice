import unittest
from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(prices[i] - min_price, max_profit)
        min_price = min(prices[i], min_price)

    return max_profit
    
class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_case_2(self):
        self.assertEqual(maxProfit([7, 6, 4, 3, 1]), 0)

if __name__ == '__main__':
    unittest.main()