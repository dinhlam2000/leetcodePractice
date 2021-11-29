def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dicBool = [False] * (len(s) + 1)
    dicBool[0] = True

    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if s[j:i] in wordDict and dicBool[j]:
                dicBool[i] = True
                break

    return dicBool[-1]