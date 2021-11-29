
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # root node be empty
        return self.isBST(root, float('-inf'), float('inf'))

    # Returns true if given tree is BST
    def isBST(self, root, min_, max_):

        # Base condition
        if (root == None):
            return True

        # if left node exist then check it has
        # correct data or not i.e. left node's data
        # should be less than root's data
        if root.val <= min_ or root.val >= max_:
            return False

        # check recursively for every node.
        return self.isBST(root.left, min_, root.val) and self.isBST(root.right, root.val, max_)
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # root node be empty
    return self.isBST(root, float('-inf'), float('inf'))


# Returns true if given tree is BST
def isBST(self, root, min_, max_):
    # Base condition
    if (root == None):
        return True

    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if root.val <= min_ or root.val >= max_:
        return False

    # check recursively for every node.
    return self.isBST(root.left, min_, root.val) and self.isBST(root.right, root.val, max_)