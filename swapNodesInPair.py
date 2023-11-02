class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        head = head.next
        if head.next is None:
            head.next = p
            p.next = None
        else:
            p.next = p.next.next
            head.next = p
            head.next.next = self.swapPairs(head.next.next)
        return head