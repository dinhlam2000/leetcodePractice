#have two arrays one for digit and one for letter
#check the log if it's digit then add it to digit order
#else add it to lexi as a tuple
#source lexi using its tuple, with the second component first and if they're equal sort it with first component then
#add lexi and digit then return that

def reorderLogFiles(logs):
    digitOrder = []
    lexiOrder = []
    for words in logs:
        splitValue = words.split(" ")
        digitOrLetter = splitValue[1][0]
        if "0" <= digitOrLetter <= "9":
            digitOrder.append(words)
        else:
            tupleForLexi = []
            tupleForLexi.append(splitValue[0])
            tupleForLexi.append(" ".join(splitValue[1:len(splitValue)]))
            lexiOrder.append(tupleForLexi)

    lexiOrder = sorted(lexiOrder, key=lambda x: (x[1], x[0]))
    lexiOrder = list(map(lambda x: x[0] + " " + x[1], lexiOrder))
    # digitOrder = list(map(lambda x: x[0] + " " + x[1],digitMap.items()))
    return lexiOrder + digitOrder

if __name__ == "__main__":

    log = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    import pdb; pdb.set_trace()

    print(reorderLogFiles(log))
    print("haha")