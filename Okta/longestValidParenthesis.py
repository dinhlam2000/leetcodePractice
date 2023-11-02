class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # have a stack that maintains when it was last opened that has not been closed
        # when reaching a closed parenthesis, the last opened Index on the stack is the valid opened parenthesis
        # have a validParenthesis array to determine the segments that are valid
        # We can structure our algorithm to assume everything is invalid, then scan through the string, marking substrings as valid
        # whenever a closing parentheses is matched to an opening parentheses., set the indices inside the validParenthesis to be true
        # Count and return the longest unbroken sequence of true values in validParenthesis
        stack = []
        validParenthesis = [False] * len(s)
        for i in range(len(s)):
            current_char = s[i]
            if current_char == ')':
                if len(stack) > 0 and s[stack[-1]] == '(':
                    lastOpenedIndex = stack.pop()
                    validParenthesis[lastOpenedIndex], validParenthesis[i] = True, True

            else:
                stack.append(i)
        maxLength = 0
        currentLength = 0
        for value in validParenthesis:
            if value == True:
                currentLength = currentLength + 1
            else:
                currentLength = 0
            maxLength = max(maxLength, currentLength)

        return maxLength




