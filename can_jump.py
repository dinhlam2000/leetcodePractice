#You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

#START WITH THE second to last value AND SEE HOW FAR IT CAN JUMP, if it passes the target then that set the target as that new index etc.
def canJump(self, nums: List[int]) -> bool:
    if len(nums) <= 1:
        return True
    target = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):  
        max_length = i + nums[i]
        if max_length >= target:
            target = i

    return target == 0