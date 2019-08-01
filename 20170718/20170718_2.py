# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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
    def getVal(self, l):
        v = 0
        while l:
            v += l.val
            l = l.next
            if l:
                v *= 10
        return v
    def addTwoNumbers(self, l1, l2):
        v = self.getVal(l1) + self.getVal(l2)        
        return self.make_list(str(v))

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        a = s.make_list("7243")
        b = s.make_list("564")
        self.assertEqual(s.print_list(s.addTwoNumbers(a, b)), s.print_list(s.make_list("7807")))

if __name__ == "__main__":
    unittest.main()
