#create an array from of n + 1 size to indicate all possibilities of reaching each number with the least amount of perfect ssquares
#then go through that array and make sure to choose all the amount of time it takes to target - value and get the minimum of the current way
class Solution:
    def numSquares(self, n):
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for s in range(1, target+1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])


        return dp[n]