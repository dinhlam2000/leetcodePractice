# def subsets(nums: List[int]) -> List[List[int]]:
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

if __name__ == '__main__':
    input = [1,2]
    print(subsets(input))

