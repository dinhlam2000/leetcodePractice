class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countSingle(root):
    # fill in this method
    # current node
    # if all children are same value as current node -> + 1 counter
    # recursively until we hit None on both the left and right children side
    count = [0]
    countSing(root, count)
    return count[0]


def countSing(root, count):
    if root == None:
        return True
    left = countSing(root.left, count)
    right = countSing(root.right, count)
    if left == False or right == False:
        return False
    if root.left and root.left.data != root.data:
        return False
    if root.right and root.right.data != root.data:
        return False
    count[0] += 1
    return True
