#use backtracking

def generateParenthesis(self, n: int) -> List[str]:
    result = []

    def backTracking(result, answer, amountOfOpen, amountOfClosed, maxValue):
        if (len(answer) == 2 * maxValue):
            result.append(answer)
            return

        if amountOfOpen < maxValue:
            backTracking(result, answer + "(", amountOfOpen + 1, amountOfClosed, maxValue)
        if amountOfClosed < amountOfOpen:
            backTracking(result, answer + ")", amountOfOpen, amountOfClosed + 1, maxValue)

    backTracking(result, "", 0, 0, n)
    return result
