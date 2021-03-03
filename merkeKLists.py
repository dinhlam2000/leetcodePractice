#brute force, by searching through the head of each node
#whatever head is smallest, make sure we indicate which index of that node is
# then create a new node from it using that head
#move that smallest head to the next pointer
# then the new node next pointer will be recursively until we cant find another head

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    indexNode = -1
    smallest = float("inf")

    for i in range(len(lists)):
        if (lists[i] and lists[i].val < smallest):
            indexNode = i
            smallest = lists[i].val
    # found the smallest head and the corresponding index

    if indexNode != -1:
        newListNode = ListNode(lists[indexNode].val)
        lists[indexNode] = lists[indexNode].next
        newListNode.next = self.mergeKLists(lists)
        return newListNode
