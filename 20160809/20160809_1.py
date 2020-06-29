# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def make_list(self, vv):
        a = [ListNode(int(v)) for v in vv]
        for i in range(len(a)-1):
            a[i].next = a[i+1]
        return a[0]
    def print_list(self, l):
        s = ""
        while l:
            # print(l.val, end='')
            s += "%d" % l.val
            if l.next:
                # print(" -> ", end='')
                s += " -> "
            l = l.next
        # print()
        return s
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        node = dummy
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if not l1:
            node.next = l2
        if not l2:
            node.next = l1
        return dummy.next

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        a = s.make_list("124")
        b = s.make_list("134")
        self.assertEqual(s.print_list(s.mergeTwoLists(a, b)), s.print_list(s.make_list("112344")))

if __name__ == "__main__":
    unittest.main()
