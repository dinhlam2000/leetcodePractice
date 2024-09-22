"https://leetcode.com/problems/maximum-subarray/description/"

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentValue = maxValue = nums[0]
        for i in range(1, len(nums)):
            currentValueSum = currentValue + nums[i]
            currentValue = max(currentValueSum, nums[i])
            maxValue = max(maxValue, currentValue)

        return maxValue
        