#start with the smallest head of two node
#go through until one of the two node hits null
#during the loop map the head to he value of two node and pick the smaller one
#then once leave the loop, make next the node that isnt null

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode()
    head = result
    while l1 and l2:

        if (l1.val <= l2.val):
            result.next = l1
            l1 = l1.next
        else:
            result.next = l2
            l2 = l2.next
        result = result.next

    if l1:
        result.next = l1
    if l2:
        result.next = l2

    return head.next

