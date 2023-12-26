import unittest
class Solution:
    def judgeSquareSum(c: int) -> bool:
        if c == 0:
            return True

        a = 1
        while a * a <= c:
            b_squared = c - a * a
            # check if b is a perfect square value
            b = int(b_squared ** 0.5)
            if b * b == b_squared:
                return True
            a += 1

        return False

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution.judgeSquareSum(5), True)

    def test_case_2(self):
        self.assertEqual(Solution.judgeSquareSum(1), True)

    def test_case_3(self):
        self.assertEqual(Solution.judgeSquareSum(0), True)

    def test_case_4(self):
        self.assertEqual(Solution.judgeSquareSum(13), True)

    def test_case_5(self):
        self.assertEqual(Solution.judgeSquareSum(14), False)

if __name__ == '__main__':
    unittest.main()