from typing import List
def wordBreak(s: str, wordDict: List[str]) -> bool:
    dicBool = [False] * (len(s) + 1)
    dicBool[0] = True
    import pdb; pdb.set_trace()
    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if s[j:i] in wordDict and dicBool[j]:
                dicBool[i] = True
                break

    return dicBool[-1]

wordBreak('abcleetcode', ['leet','code', 'abc'])
