class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        odds = oddl = head
        evens = evenl = head.next
        while True:
            if evenl.next:
                oddl.next = evenl.next
                oddl = evenl.next
            else:
                oddl.next = None
                break
            if oddl.next:
                evenl.next = oddl.next
                evenl = oddl.next
            else:
                evenl.next = None
                break
        oddl.next = evens
        return odds

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

s = Solution()
node_vals = [1,2,3,4,5,6,7,8]
head = makeList(node_vals)

print "%25s %25s %25s" % ("input", "Expected", "Result")
print "%25s %25s %25s" % (node_vals, "[1, 3, 5, 7, 2, 4, 6, 8]", printList(s.oddEvenList(head)))