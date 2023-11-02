    #have a queue that starts with a root
#then add the queue to a temp list
#go through that temp list and see if there's any value that root in left and right
#if there is append those vlaues to queue
#insert the layer to the beginning of result everytime we go through the new queue

def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    if root == None:
        return []
    result = []
    queue = [root]

    while (len(queue) != 0):

        layer = []

        for index in range(len(queue)):
            rootVal = queue.pop(0)
            layer.append(rootVal.val)
            if rootVal.left != None:
                queue.append(rootVal.left)
            if rootVal.right != None:
                queue.append(rootVal.right)

        result.insert(0, layer)

    return result
