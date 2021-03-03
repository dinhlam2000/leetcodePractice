#add the courses to a map with weight, where its weight is how many times it was mapped to
#then go through the map and get the heaviest key out and append that key to result
#then delete that key
#then result should contain that

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    result = []
    while numCourses > 0 and len(prerequisites) == 0:
        numCourses = numCourses - 1
        result.append(numCourses)

    weightedEach = {}
    for item in prerequisites:
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

    return result


