class Solution:
    def jump(self, nums: List[int]) -> int:
        # start having a sliding window from left to right
        # basically from left to right we check what's the max jump distance it can generate
        # that would be the new right value and then we would check every possible case within that window
        # that the initial jump can reach to and so we can calculate the max possible output in jump total
        # we do that until right reaches the end
        l,r = 0,0
        result = 0
        while r < len(nums) - 1:
            maxJump = 0
            for i in range(l,r + 1,1):
                maxJump = max(maxJump, nums[i] + i)
            r = maxJump
            l = l + 1
            result = result + 1
        return result

        # l = 1
        # r = 0, 2
        # maxJump = 0 -> 2