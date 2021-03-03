#check if each node is the same as the subtree
#check is same by go through all elements  left and right and if both reaches None then yes it's same
#if one reaches none before then no


def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    if t is None:
        return True
    if s is None and t is None:
        return True
    if s is None and t is not None:
        return False
    return self.checkSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


def checkSameTree(self, s, t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False

    return s.val == t.val and self.checkSameTree(s.left, t.left) and self.checkSameTree(s.right, t.right)