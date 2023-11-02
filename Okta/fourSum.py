class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        def helper(n, result, combination, currentNums, target):
            if n == 2:
                left = 0
                right = len(currentNums) - 1
                while left < right:
                    sum_value = currentNums[left] + currentNums[right]
                    if sum_value == target:
                        result.append(combination + [currentNums[left], currentNums[right]])
                        left = left + 1
                        while currentNums[left] == currentNums[left - 1] and left < right:
                            left = left + 1
                    elif sum_value < target:
                        left = left + 1
                    else:
                        right = right - 1
            else:
                for i in range(len(currentNums)):
                    if i == 0 or (i > 0 and currentNums[i] != currentNums[i - 1]):
                        helper(n - 1, result, combination + [currentNums[i]], currentNums[i + 1:],
                               target - currentNums[i])

        helper(4, result, [], nums, target)
        return result