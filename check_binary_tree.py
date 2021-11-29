def checkTree(root: Node) -> bool:
    # DFS left node and making sure it's less than root node
    # DFS right node nad making sure it's greater than root node
    # if it's less than and its children have its own children
    # then recursively call the same thing
    def helper(node: Node, min: float, max: float):
        if node == None:
            return True
        if node.value < min or node.value > max:
            return False

        return helper(node.left, min, node.value) and helper(node.right, node.value, max)

    return helper(root, float('-inf'), float('inf'))
