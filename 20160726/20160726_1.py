class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next and node.next.next:
            first = node.next
            second = node.next.next
            first.next = second.next
            second.next = first
            node.next = second
            node = node.next.next
        return dummy.next
