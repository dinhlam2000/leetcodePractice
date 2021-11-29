#create a dictionary with each number corresponds to the right letters
#use backtracking to append to the output

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        output = []
        import pdb; pdb.set_trace()
        def backTrack(combination, digitList):
            if len(digitList) == 0:
                output.append(combination)
            else:
                for letter in phone[digitList[0]]:
                    backTrack(combination + letter, digitList[1:])

        if digits:
            backTrack("", digits)

        return output

print(Solution().letterCombinations('234'))