import unittest
from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    ans = 0

    g.sort(reverse=True)
    s.sort(reverse=True)

    g_ptr = 0
    s_ptr = 0
    while (s_ptr < len(s) and g_ptr < len(g)):
        if s[s_ptr] >= g[g_ptr]:
            s_ptr += 1
            ans += 1
        g_ptr += 1

    return ans

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findContentChildren([1, 2, 3], [1, 1]), 1)
        
    def test_case_2(self):
        self.assertEqual(findContentChildren([1, 2], [1, 1]), 1)
        
    def test_case_3(self):
        self.assertEqual(findContentChildren([5, 5, 3], [4]), 1)
        
    def test_case_4(self):
        self.assertEqual(findContentChildren([3,2,1], [2,2]), 2)

if __name__ == '__main__':
    unittest.main()