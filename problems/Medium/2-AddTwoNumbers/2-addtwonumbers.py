from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        head.next = l1

        carry = 0
        while(l1 != None and l2 != None):
            if (l2 != None):
                sum = l1.val + l2.val
                if carry:
                    sum += carry
                if sum >= 10:
                    carry = 1
                    sum -= 10
                else:
                    carry = 0
                l1.val = sum
                l2 = l2.next
            if l1.next == None and l2 == None and carry:
                l1.next = ListNode(1)
                carry = 0

            if l1.next == None:
                l1.next = l2
                l2 = None

            l1 = l1.next

        while l1 != None and carry:
            sum = l1.val + carry
            if sum >= 10:
                carry = 1
                sum -= 10
            else:
                carry = 0
            l1.val = sum

            if l1.next == None and carry:
                l1.next = ListNode(1)
                break

            l1 = l1.next

        return head.next
        


class MyTest(unittest.TestCase):
    def test_case_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        ans = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(ans.val, 7)
        self.assertEqual(ans.next.val, 0)
        self.assertEqual(ans.next.next.val, 8)
        self.assertEqual(ans.next.next.next, None)

    def test_case_2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        ans = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(ans.val, 0)
        self.assertEqual(ans.next, None)

    def test_case_3(self):
        l1 = ListNode(5)
        l2 = ListNode(5)
        ans = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(ans.val, 0)
        self.assertEqual(ans.next.val, 1)
        self.assertEqual(ans.next.next, None)

    def test_case_4(self):
        l1 = ListNode(1, ListNode(8))
        l2 = ListNode(0)
        ans = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(ans.val, 1)
        self.assertEqual(ans.next.val, 8)
        self.assertEqual(ans.next.next, None)
    

if __name__ == '__main__':
    unittest.main()