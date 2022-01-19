# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def subsets(nums):
    # can contain an empty array
    # cannot contain duplicate number
    # input = [1, 2] -> [] , [1], [2], [1,2]

    # FIRST DECISION: INCLUDE THE VALUE
    # SECOND DECISION: NOT INCLUDE THE VALUE

    # [] => 1 
    #            -> FIRST DECISION [1] increment index 
    #            ->                   --> FIRST DECISION: [1,2] --> 
    #            ->                   --> SECOND DECISION: [1]       
    #            -> SECOND DECISION [] increment index
    #            ->                   --> FIRST DECISION: [2]
    #            ->                   --> SECOND DECISION: []

    # index = 1
    # subsets = [[1,2], [1], [2], [] ]
    # current_data []
    subsets = []
    current_data = []
    generateSubsets(0, nums, subsets, current_data)
    return subsets


def generateSubsets(index, nums, subsets, current_data):
    if index >= len(nums):
        subsets.append(current_data.copy())
        return

    # first decision of including
    current_data.append(nums[index])
    generateSubsets(index + 1, nums, subsets, current_data)

    # make a second decision of not including
    current_data.pop()
    generateSubsets(index + 1, nums, subsets, current_data)


def solution(A):
    # write your code in Python 3.6
    all_subsets = subsets(A)
    all_subsets = list(filter(lambda x: len(x) > 0, all_subsets))
    size_possible = []
    import pdb; pdb.set_trace()
    for index, subset in enumerate(all_subsets):
        value = subset[0]
        for num in subset:
            value = value & num
        if value > 0:
            size_possible.append(len(subset))

    return max(size_possible)

input_value = [13,7,2,8,3]
solution(input_value)