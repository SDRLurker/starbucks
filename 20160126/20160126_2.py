# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def make_two_list(self, aa, bb, cc, bi):
        a = [ListNode(int(v)) for v in aa]
        ai_dic = {}
        for i in range(len(a)-1):
            a[i].next = a[i+1]
            ai_dic[aa[i]] = i
        i = len(a) - 1
        ai_dic[aa[i]] = i
        b = [ListNode(int(v)) for v in bb]
        for i,c in enumerate(bb):
            if i == bi:
                b[i-1].next = a[ai_dic[c]]
                break
            if 0 < i < len(bb):
                b[i-1].next = b[i]
        return (a[0],b[0],b[bi-1].next if bi >= 0 else None)
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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a_set = set()
        while headA:
            a_set.add(headA)
            headA = headA.next
        while headB:
            if headB in a_set:
                return headB
            headB = headB.next
        return None

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        a,b,i = s.make_two_list("41845","501845","8",3)
        print(s.print_list(a))
        print(s.print_list(b))
        print("---")
        a,b,i = s.make_two_list("09124","324","2",1)
        print(s.print_list(a))
        print(s.print_list(b))
        print("---")
        a,b,i = s.make_two_list("264","15","",-1)
        print(s.print_list(a))
        print(s.print_list(b))
        self.assertEqual(s.getIntersectionNode(a,b),None)

if __name__ == "__main__":
    unittest.main()
