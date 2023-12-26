import unittest
from typing import List

def findRelativeRanks(score: List[int]) -> List[str]:
    ans = []
    # {score: placement}
    score_map = {}

    # O(nlogn)
    sorted_score = sorted(score, reverse=True)

    # O(n)
    for i in range(len(sorted_score)):
        score_map[sorted_score[i]] = i + 1

    # O(n)
    for i in range(len(score)):
        placement_str = str(score_map[score[i]])
        if placement_str == "1":
            placement_str = "Gold Medal"
        if placement_str == "2":
            placement_str = "Silver Medal"
        if placement_str == "3":
            placement_str = "Bronze Medal"
            
        ans.append(placement_str)

    return ans

class MyTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findRelativeRanks([5, 4, 3, 2, 1]), ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])

    def test_case_2(self):
        self.assertEqual(findRelativeRanks([10,3,8,9,4]), ["Gold Medal","5","Bronze Medal","Silver Medal","4"])

    def test_case_3(self):
        self.assertEqual(findRelativeRanks([0]), ["Gold Medal"])

    def test_case_4(self):
        self.assertEqual(findRelativeRanks([1,3,2]), ["Bronze Medal","Gold Medal","Silver Medal"])

if __name__ == '__main__':
    unittest.main()