def longestPalindrome(s: str) -> str:
    if (len(s) == 0): return ""
    if len(s) == 1: return s
    start = 0
    end = 0
    maxLen = 0
    for index, char in enumerate(s):
        len1 = expandFromMiddle(index, index, s)
        len2 = expandFromMiddle(index, index + 1, s)
        maxLen = max(len1, len2)
        if maxLen > (end - start):
            start = index - (maxLen - 1) / 2
            end = index + maxLen / 2 + 1
    print("haha")
    start = int(start)
    end = int(end)
    return s[start:end]


def expandFromMiddle(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left = left - 1
        right = right + 1
    return right - left - 1

def mostCommonWord(paragraph,banned):

    wordCount = {}

    for word in paragraph.split():

        formattedWord = "".join(map(lambda x: x if x.isalpha() else "", word))
        formattedWord = formattedWord.lower()
        if (formattedWord not in wordCount):
            wordCount[formattedWord] = 1
        else:
            newValue = wordCount[formattedWord]
            newValue = newValue + 1
            wordCount[formattedWord] = newValue
    max_key = max(wordCount, key=wordCount.get)
    return max_key

def findOrder(numCourses, prereq):

    result = []
    weightedEach = {}

    for item in prereq:
        if item[0] not in weightedEach:
            weightedEach[item[0]] = 0
        if item[1] not in weightedEach:
            weightedEach[item[1]] = 1


        else:
            newWeight = weightedEach.get(item[1])
            newWeight = newWeight + 1
            weightedEach[item[1]] = newWeight

    while len(weightedEach) != 0:
        heaviest_Key = max(weightedEach, key=weightedEach.get)
        result.append(heaviest_Key)
        del weightedEach[heaviest_Key]

    if len(result) == numCourses:
        return result




if __name__ == "__main__":
    import pdb; pdb.set_trace()
    # longsetPal = longestPalindrome(s="babad")
    # print(longsetPal)
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # print(mostCommonWord(paragraph,banned))
    numCourse = 4
    prereq = [[1,0],[2,0],[3,1],[3,2]]
    print(findOrder(numCourse,prereq))