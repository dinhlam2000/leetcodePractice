#make the same copy node but that the value of random and next are none and put each node in a dictionary
#now go through the head one more time
#point the current of the new copied node next to dictionary[current.next]
#do same with random
#return clonedHead[head] which is the dictionary

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if head == None:
            return None

        clonedHead = {}
        current = head
        while current != None:
            clonedHead[current] = Node(current.val, None, None)
            current = current.next

        current = head

        while current != None:
            if current.next:
                clonedHead[current].next = clonedHead[current.next]
            if current.random:
                clonedHead[current].random = clonedHead[current.random]
            current = current.next

        return clonedHead[head]