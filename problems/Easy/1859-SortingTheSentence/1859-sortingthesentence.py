import unittest

def sortSentence( s: str) -> str:
    words = s.split(" ")
    ans = [""] * len(words)
    for word in words:
        # this is the 1-based index
        index = int(word[len(word)-1:])
        ans[index - 1] = word[:len(word)-1]

    return " ".join(ans)

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sortSentence("is2 sentence4 This1 a3"), "This is a sentence")

if __name__ == '__main__':
    unittest.main()