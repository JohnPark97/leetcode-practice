import unittest
def areAlmostEqual(s1: str, s2: str) -> bool:
        occurrences = {}

        for i in range(len(s1)):
            occurrences.setdefault(s1[i], 0)
            occurrences[s1[i]] += 1

        tries = 3
        for i in range(len(s2)):
            if not occurrences.get(s2[i]) or occurrences.get(s2[i]) == 0:
                return False
            if s1[i] != s2[i]:
                tries -= 1
            occurrences[s2[i]] -= 1

        if tries <= 0:
            return False    
        
        return True

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(areAlmostEqual("bank", "kanb"), True)

    def test_case_2(self):
        self.assertEqual(areAlmostEqual("attack", "defend"), False)

    def test_case_3(self):
        self.assertEqual(areAlmostEqual("kelb", "kelb"), True)

if __name__ == '__main__':
    unittest.main()