def find_sum_zero_subsets(arr):
    # fill in
    # arr contain no values at all?
    # arr contain only 1 value --> has to be zero
    # brute force is to get all the possible subsets
    # return the ones that are summing up to zero

    # another way:
    # hash map --> store all the sum value we have seen before
    # iterate through array and find the sum total we have seen at that point
    # if that sum is seen in the hash map before --> we can exTRACT out all the values at that point
    # that is seen after until
    # 3,5,-2,-4,7,-1
    # sum [3,8,6,2,9,8
    hash_sum = {}
    sum_t = 0
    result = []
    for index, value in enumerate(arr):
        sum_t = sum_t + value
        if sum_t == 0:
            result.append([0, index])
        if sum_t in hash_sum:
            start_index = hash_sum[sum_t]
            result.append([start_index + 1, index])
        hash_sum[sum_t] = index

    return result

# print(find_sum_zero_subsets([1, 2, 0, -3, -2]))
