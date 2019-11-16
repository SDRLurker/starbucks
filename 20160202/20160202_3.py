class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
        l3 = None
        l3_start = None
        carry = 0
        while l1 or l2 or carry:
            v = 0            
            if l1:
                v += l1.val
            if l2:
                v += l2.val
            v += carry
            if not l3:
                l3 = ListNode(v % 10)
                l3_start = l3
            else:                
                l3.next = ListNode(v % 10)
                l3 = l3.next
            carry = v // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return l3_start

def makeList(node_vals):
    list_nodes = []
    for i in node_vals:
        node = ListNode(i)
        list_nodes.append(node)
    for i in xrange(len(node_vals)-1):
        list_nodes[i].next = list_nodes[i+1]
    return list_nodes[0]

def printList(head):
    cur = head
    array = []
    while cur:
       array.append(cur.val)
       cur = cur.next
    return array

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        l1 = makeList([2,4,3])
        l2 = makeList([5,6,4])
        self.assertEqual(printList(s.addTwoNumbers(l1,l2)), [7,0,8])
        l1 = makeList([5])
        l2 = makeList([5])
        self.assertEqual(printList(s.addTwoNumbers(l1,l2)), [0,1])
        l1 = makeList([1])
        l2 = makeList([9,9])
        self.assertEqual(printList(s.addTwoNumbers(l1,l2)), [0,0,1])

if __name__ == "__main__":
    unittest.main()
