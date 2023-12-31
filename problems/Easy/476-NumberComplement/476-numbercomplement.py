import unittest

def findComplement(num: int) -> int:
    binary = bin(num)[2:]
    complement = "".join(["1" if bit == "0" else "0" for bit in binary])
    return int(complement, 2)
    
class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findComplement(5), 2)

    def test_case_2(self):
        self.assertEqual(findComplement(1), 0)

    def test_case_3(self):
        self.assertEqual(findComplement(0), 1)

if __name__ == '__main__':
    unittest.main()