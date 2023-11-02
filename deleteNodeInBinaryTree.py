"""
First we need to find our node in tree, so we just traverse it until root.val == key.
Case 1: node do not have any children, like 1, 8, 11, 14, 6 or 18: then we just delete it and nothing else to do here.
Case 2: node has left children, but do not have right, for example 3 or 20. In this case we can just delete this node and put connection betweeen its parent and its children:
for example for 3, we put connection 5->1 and for 20 we put connection 17->18. Note, that the property of BST will be fulfilled,
because for parent all left subtree will be less than its value and nothing will change for others nodes.
Case 3: node has right children, but do not have left, for example 13 and 17. This case is almost like case 2: we just can delete node and reconnect its parent with its children.
Case 4: node has both children, like 12, 5, 7, 9 or 15. In this case we can not just delete it. Let us consider node 5. We want to find succesor of this node:
the node with next value, to do this we need to go one time to the right and then as left as possible. For node 5 our succesor will be 6:
 we go 5->7->6. How we can delete node 5 now? We swap nodes 5 and 6 (or just put value 6 to 5) and then we need to deal with new tree,
 where we need to delete node which I put in square. How to do it? Just understand, that this node do not have left children, so it is either Case 1 or Case 3, which we already can solve.
"""
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # base case
        if not root: return None

        # base case (almost) with key found
        if root.val == key:
            # 1.a leaf or single child
            if not root.right: return root.left

            # 1.b leaf or single child
            if not root.left: return root.right

            # 2: both child node exist
            if root.left and root.right:
                # 2.a.1: start with right node of deleted node
                temp = root.right

                # 2.a.2: find minimum node in left subtree
                # we are going to replace minimum in left subtree with value at root
                while temp.left:
                    temp = temp.left

                # 2.b: replace value with minimum value in right subtree
                root.val = temp.val

                # 2.c: ** key step ** recurse on root.right but with key  = root.val (min val in right subtree)
                root.right = self.deleteNode(root.right, root.val)

        # recursion steps
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root