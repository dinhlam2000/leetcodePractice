"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

"""

def minOperations(self, nums: List[int], x: int) -> int:

        # find the sub arrays that add up to total - x
        # once we find that sub array
        # KEY: we can get the answer by grabbing the length of that sub array and subtract that from the length of original array

        # edge case:
        # 1. if no sub array is going to add up to total - x
        #   and sum of subarray all the sudden is greater than total - x
        #   then we move the left pointer up until the currentSum is no longer greater than

        result = -1
        currentSum = 0
        left = 0

        targetedSubArraySum = sum(nums) - x
        if targetedSubArraySum == 0:
            return len(nums)
        for right in range(len(nums)):
            currentSum = currentSum + nums[right]
            while currentSum > targetedSubArraySum and left < right:
                currentSum = currentSum - nums[left]
                left = left + 1
            if currentSum == targetedSubArraySum:
                result = max(result, right - left + 1)
        return len(nums) - result if result != -1 else result
