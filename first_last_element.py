def searchRange(nums, target):
    left = 0
    right = len(nums) - 1

    found_point = -1
    import pdb; pdb.set_trace()
    while left <= right:
        mid_point = left + (right - left) // 2

        mid_point_value = nums[mid_point]
        print(mid_point)
        if mid_point_value > target:
            right = mid_point - 1
        elif mid_point_value < target:
            left = mid_point + 1
        else:
            found_point = mid_point
            break

    if found_point != -1:
        temp_found_point_left = found_point
        temp_found_point_right = found_point
        while nums[temp_found_point_left] == target:
            temp_found_point_left = temp_found_point_left - 1
        while nums[temp_found_point_right] == target:
            temp_found_point_right = temp_found_point_right + 1

        return [temp_found_point_left + 1, temp_found_point_right - 1]
    if right > left:
        if left == 0:
            value = nums[0]
            if value == target:
                return [0,0]
        if right == len(nums) - 1:
            value = nums[-1]
            if value == target:
                return [len(nums)-1, len(nums)-1]
    return [-1, -1]


print(searchRange([6,7,7,8,8,10,10,10], 8))


def numberOfWays(arr, k):
    # Write your code here
    # arr can contain negative values
    # arr have no values at all -> contain no values at all
    # returning the amount of pairs

    # mapping how many times a certain values occur
    # algebraic expression -> looking at current value in the arr -> target + current = k
    # target = k - current
    # target is in the map -> add to result the amount of times target occur
    # target is the same as current -> add the result to the amount times target occur - 1
    # [2] k = 4

    result = 0
    from collections import defaultdict
    value_map = defaultdict(int)
    for value in arr:
        value_map[value] += 1
    # having a value map -> value : count

    for value in arr:
        target = k - value
        if target in value_map:
            count_target = value_map[target]
            if target == value:

                result = result + count_target - 1

            else:
                result = result + count_target

    return result // 2

