class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        res = ListNode(head.val)
        p = res
        while head:            
            if head.next:
                if head.val != head.next.val:
                    p.next = ListNode(head.next.val)
                    p = p.next
            head = head.next
        return res

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
        in_nodes = makeList([1,1,2])
        self.assertEqual(printList(s.deleteDuplicates(in_nodes)), [1,2])
        in_nodes = makeList([1,1,2,3,3])
        self.assertEqual(printList(s.deleteDuplicates(in_nodes)), [1,2,3])

if __name__ == "__main__":
    unittest.main()
