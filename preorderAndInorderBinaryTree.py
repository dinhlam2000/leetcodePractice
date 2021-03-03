#go through the list of preorder and inorder
#construct the tree and the root is always preorder[current value]
#then find where the root is in the inorder
#then indicate the index for it to determine the left and right node
#then root.left will start from the next preOrder element and same instart until the index Root -1
#root right will be everything on the right side, but prestart is tricky as it's prestart + indexRoot - instart + 1

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    return self.constructTree(0, 0, len(inorder) - 1, preorder, inorder)


def constructTree(self, prestart: int, instart: int, inend: int, preorder: List[int], inorder: List[int]):
    if (prestart > len(preorder) - 1 or instart > inend):
        return 0;

    root = TreeNode(preorder[prestart])
    i = instart
    indexRoot = 0
    while (i <= inend):
        if root.val == inorder[i]: indexRoot = i
        i += 1

    root.left = self.constructTree(prestart + 1, instart, indexRoot - 1, preorder, inorder)
    root.right = self.constructTree(prestart + indexRoot - instart + 1, indexRoot + 1, inend, preorder, inorder)
    return root

