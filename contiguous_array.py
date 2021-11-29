# Maintain a stack such that it always contains the index for the last maximum encountered.
# If the next element is greater than the arr[stack.peek()] then pop the top of the stack till we find a equal or greater element.
# * If stack is empty then it means that the current element is the maximum of all and hence there are (current index + 1) possible arrays meeting the criteria.
# * If stack is not empty, then (current index - stack top) will be possible arrays for the index position
# Repeat the same steps from end of the array to get the final solution.
def count_subarrays(arr):
    import pdb; pdb.set_trace()
    n = len(arr)
    res = [1] * n
    stack = [-1]
    # left
    for i in range(n):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += i - stack[-1] - 1
        stack.append(i)

    # from right
    stack = [n]
    for i in range(n - 1, -1, -1):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += stack[-1] - i - 1
        stack.append(i)
    import pdb; pdb.set_trace()
    return res

count_subarrays([3,4,1,6,2])