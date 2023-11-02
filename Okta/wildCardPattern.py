class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        # print('dp', dp)
        for row in range(1,len(dp)):
            dp[row][0] = False
        for column in range(1,len(dp[0])):
            dp[0][column] = dp[0][column - 1] if p[column-1] == '*' else False
        # print('dp2', dp)
        for row in range(1,len(dp)):
            for column in range(1,len(dp[row])):
                sChar = s[row-1]
                pChar = p[column - 1]
                if pChar == '*':
                    dp[row][column] = dp[row-1][column] or dp[row][column - 1]
                else:
                    if pChar == '?' or sChar == pChar:
                        dp[row][column] = dp[row-1][column-1]
                    else:
                        dp[row][column] = False
        # print(dp)
        return dp[-1][-1]