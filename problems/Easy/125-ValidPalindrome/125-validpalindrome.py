import unittest

def isPalindrome(s: str) -> bool:
    # alnum_str = ''.join(char for char in s if char.isalnum()).lower()

    left = 0
    right = len(s) - 1

    while left < right:
        while not s[left].isalnum():
            left += 1
            if left > right:
                return True
        while not s[right].isalnum():
            right -= 1
            if right < left:
                return True
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

class MyTest(unittest.TestCase):
    def test_case_1(self):
        s = "race a car"
        self.assertEqual(isPalindrome(s), False)
    
    def test_case_2(self):
        s = "A man, a plan, a canal: Panama"
        self.assertEqual(isPalindrome(s), True)

    def test_case_3(self):
        s = "0P"
        self.assertEqual(isPalindrome(s), False)

    def test_case_4(self):
        s = ".....,,,,,,,."
        self.assertEqual(isPalindrome(s), True)

if __name__ == '__main__':
    unittest.main()