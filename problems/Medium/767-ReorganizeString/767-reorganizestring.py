import unittest
from math import ceil

class MyTest(unittest.TestCase):
    def reorganizeString(self, s: str) -> str:
        map = {}
        ans = [''] * len(s)

        for char in s: 
            map.setdefault(char, 0)
            map[char] += 1
            if map.get(char) > ceil(len(s) / 2):
                return ""
        # sort the map in Descending order by values
        desc_map = dict(sorted(map.items(), key=lambda x: x[1], reverse=True))

        i = 0
        for key, val in desc_map.items():
            while val > 0:
                if i >= len(s):
                    i = 1
                ans[i] = key
                val -= 1
                i += 2

        return ''.join(ans)
    
    def test_case_1(self):
        self.assertEqual(self.reorganizeString("aab"), "aba")
    
    def test_case_2(self):
        self.assertEqual(self.reorganizeString("aaabc"), "abaca")
    
    def test_case_3(self):
        self.assertEqual(self.reorganizeString("a"), "a")
    
    def test_case_4(self):
        self.assertEqual(self.reorganizeString("aaa"), "")
        

if __name__ == '__main__':
    unittest.main()