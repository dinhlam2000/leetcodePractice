#expand from the middle of the current char
#make sure you expand with two length, one from itself, and the other length is from itself and the character next to it
#expand left and right til string[left] no longer = string[right]
#get max length from len1 and len2
#then if maxLen > (end - start) which is the substrings length then change the start and end
#new start should be index - int(((maxLen - 1)/2)) test with racecar to find this formula
#new end should be index + maxLen/2 + 1 because of offset

def longestPalindrome(self, s: str) -> str:
    if (len(s) == 0): return ""
    if len(s) == 1: return s
    start = 0
    end = 0
    maxLen = 0
    for index, char in enumerate(s):
        len1 = self.expandFromMiddle(index, index, s)
        len2 = self.expandFromMiddle(index, index + 1, s)
        maxLen = max(len1, len2)
        if maxLen > (end - start):
            start = index - int(((maxLen - 1) / 2))
            end = index + maxLen / 2 + 1
    print("haha")
    start = int(start)
    end = int(end)
    return s[start:end]


def expandFromMiddle(self, left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left = left - 1
        right = right + 1
    return right - left - 1