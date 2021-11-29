class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Add any helper functions you may need here

def rotate(start, end):
    current = start
    previous = end
    while current != end:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous


def reverse(head):
    # Write your code here
    current = head
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while current:
        start = current
        while current and current.data % 2 == 0:
            current = current.next

        # needs to do the rotation right here
        if start != current:
            prev.next = rotate(start, current)

        if current:
            prev = current
            current = current.next

    return dummy.next

