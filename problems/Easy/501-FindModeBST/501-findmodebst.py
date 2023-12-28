import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: TreeNode):
    def dfs(node, values):
        if node is None:
            return

        dfs(node.left, values)
        values.append(node.val)
        dfs(node.right, values)

    values = []
    dfs(root, values)

    max_streak = 0
    curr_streak = 0
    curr_num = 0
    ans = []

    for num in values:
        if num == curr_num:
            curr_streak += 1
        else:
            curr_streak = 1
            curr_num = num

        if curr_streak > max_streak:
            ans = []
            max_streak = curr_streak

        if curr_streak == max_streak:
            ans.append(num)

    return ans


class MyTest(unittest.TestCase):
    def test_case_1(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(2), None))
        self.assertEqual(findMode(root), [2])

    def test_case_2(self):
        root = TreeNode(0)
        self.assertEqual(findMode(root), [0])

if __name__ == '__main__':
    unittest.main()
