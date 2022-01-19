class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def stringFromTree(tree):
    result = helper(tree)
    import pdb; pdb.set_trace()
    # result = "".join(result[1: len(result) - 1])
    return result


def helper(tree):
    # fill in
    if tree == None:
        return ""
    if tree.left == None and tree.right == None:
        return "[" + str(tree.val) + "]"
    if tree.left != None and tree.right == None:
        return "[" + str(tree.val) + "[" + helper(tree.left) + "]" + "]"
    if tree.right != None and tree.left == None:
        return "[" + tree.val + "[" + helper(tree.right) + "]]"
    return "[" + str(tree.val) + "[" + helper(tree.left)   + helper(tree.right)  + "]" + "]"

# '4[[1][3]]'

tree2 = Node(5)
tree2.left = Node(10)
tree2.left.left = Node(17)
tree2.left.right = Node(3)
tree2.right = Node(8)

tree1 = Node(4)
tree1.left = Node(1)
tree1.right = Node(3)

tree3 = Node(6)
tree3.left = Node(3)
# import pdb; pdb.set_trace()
print(stringFromTree(tree3))
