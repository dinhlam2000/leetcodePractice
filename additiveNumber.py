"""
Input: "199100199"
Output: true
Explanation:
The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
"""

"""
SOLUTION:
start with n1 as the first character and check everysingle n2, and add n1 + n2, to see if there's an n3 that's matched
then 
"""
class Solution:
    def helper(self, n1, n2, s, found):
        if len(s) == 0 and found:
            return True

        n3 = str(int(n1) + int(n2))
        length = min(len(n3), len(s))
        if s[0:length] == n3:
            return self.helper(n2, n3, s[length:], True)

    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num) - 1):
            n1 = num[0:i]
            if str(int(n1)) != n1:
                break
            for j in range(i + 1, len(num)):
                n2 = num[i:j]
                if (str(int(n2)) != n2):
                    break
                if self.helper(n1, n2, num[j:], False):
                    return True
        return False
