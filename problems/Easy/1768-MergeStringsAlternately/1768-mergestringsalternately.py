import unittest

def mergeAlternately(word1: str, word2: str) -> str:
    ans = ""
    for i in range(len(word1)):
        ans += word1[i]
        if i < len(word2):
            ans += word2[i]

    if len(word1) < len(word2):
        ans += word2[len(word1):]

    return ans

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(mergeAlternately("abc", "pqr"), "apbqcr")

    def test_case_2(self):
        self.assertEqual(mergeAlternately("ab", "pqrs"), "apbqrs")
    
    def test_case_3(self):
        self.assertEqual(mergeAlternately("abcd", "pq"), "apbqcd")

if __name__ == '__main__':
    unittest.main()