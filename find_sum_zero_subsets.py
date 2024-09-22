def find_sum_zero_subsets(arr, target):
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
        if sum_t == target:
            result.append([0, index])
        if (sum_t - target) in hash_sum:
            # import pdb; pdb.set_trace()
            start_indexes = hash_sum[sum_t - target]
            print(start_indexes, hash_sum, sum_t-target)
            for start_index in start_indexes:
                result.append([start_index + 1, index])
        # print(sum_t, hash_sum)

        if sum_t in hash_sum:
            hash_sum[sum_t].append(index)
        else:
            hash_sum[sum_t] = [index]
    # print(hash_sum)
    return result

# print(find_sum_zero_subsets([3,5,-2,-4,7,-1],0))
print(find_sum_zero_subsets([0,5,-5,-2,-4,7,-1],0))
# print(find_sum_zero_subsets([1,5,9,4,-13,6,9,-4,6,-11,19],6))


# print(find_sum_zero_subsets([1, 2, 0, -3, -2]))
