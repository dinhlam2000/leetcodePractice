def maxRectInHist(histArr):
    # fill in
    # can histArr contain an empty array?
    # histArr contain a negative value?
    # does it only contain integer?
    if len(histArr) == 0:
        return 0
    if len(histArr) == 1:
        return histArr[0]

    # O(n^2) --> looking at each bar, always including this current bar as max height
    # find the first left bar that has a value less than the current bar
    # find the first right bar that has a value less than current bar

    # SO OPTIMIZING THIS:
    # keeping track of the lowest left bar value index
    # keeping track of the lowest right bar value index
    # stack is going to be holding the maximum value bar of the rectangle
    # index value on top of the stack, -->
    # histogram[index] >  histogram[current]
    # popping that top index
    # else
    stack = []
    left = []
    for i in range(len(histArr)):
        if len(stack) == 0:
            left.append(0)
        else:
            while len(stack) != 0 and histArr[stack[-1]] >= histArr[i]:
                top_index = stack.pop()
            if len(stack) == 0:
                left.append(0)
            else:
                left.append(stack[-1] + 1)
        stack.append(i)
    stack = []
    right = []
    for i in range(len(histArr) - 1, -1, -1):
        if len(stack) == 0:
            right.append(len(histArr) - 1)
        else:
            while len(stack) != 0 and histArr[stack[-1]] >= histArr[i]:
                top_index = stack.pop()
            if len(stack) == 0:
                right.append(len(histArr) - 1)
            else:
                right.append(stack[-1] - 1)
        stack.append(i)
    max_area = [0] * len(histArr)
    for i in range(len(histArr)):
        width = right[-(i + 1)] - left[i] + 1
        height = histArr[i]
        max_area[i] = width * height
    print(left, right, max_area)
    return max(max_area)


print(maxRectInHist([3, 1, 4, 2, 2, 1]))

