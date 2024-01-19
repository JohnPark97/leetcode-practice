import unittest
def lengthOfLongestSubstring(s: str) -> int:
    longest = ""
    streak = 0

    for char in s:
        try:
            i = longest.index(char)
            streak = max(streak, len(longest))
            longest = longest[i + 1:]
            longest += char
        except ValueError:
            longest += char
            
    return max(streak, len(longest))

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)

    def test_case_2(self):
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)

    def test_case_3(self):
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

    def test_case_4(self):
        self.assertEqual(lengthOfLongestSubstring(" "), 1)

if __name__ == '__main__':
    unittest.main()