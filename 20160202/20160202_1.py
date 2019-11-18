class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        if n == len(arr):
            head = head.next
        else:
            arr[-n-1].next = arr[-n].next
        return head

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
        lst = makeList([1,2,3,4,5])
        self.assertEqual(printList(s.removeNthFromEnd(lst,2)), [1,2,3,5])
        lst = makeList([1,2,3,4,5])
        self.assertEqual(printList(s.removeNthFromEnd(lst,5)), [2,3,4,5])

if __name__ == "__main__":
    unittest.main()
