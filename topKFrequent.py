#map every word and add a weight to it
#then just sort the list using the -negative weight, but use key if they're equal
#sorted (-x[1], x[0])

def topKFrequent(words,k):
    result = []

    weightEachWord = {}

    for word in words:

        if word not in weightEachWord:
            weightEachWord[word] = 1
        else:
            newWeight = weightEachWord[word]
            newWeight = newWeight + 1
            weightEachWord[word] = newWeight

    weightEachWord = sorted(weightEachWord.items(), key=lambda x: (-x[1], x[0]))

    result = list(map(lambda x: x[0], weightEachWord))
    return res

if __name__ == "__main__":
    words = ["coding", "love", "leetcode", "i", "love", "i"]
    k = 3
    import pdb; pdb.set_trace()
    test = ["asd", "bdc"]

    print(topKFrequent(words,k))
    print("haha")

