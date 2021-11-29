def kClosest(points,k):
    result = {}

    for index, point in enumerate(points):
        result[index] = calculateDistance(point)
    import pdb ; pdb.set_trace()
    result = sorted(result.items(), key=lambda x: (x[1], x[0]))
    result = list(map(lambda x: x[0], result))
    import pdb; pdb.set_trace()
    finalResult = list(map(lambda x: points[x], result))
    return (finalResult[:k])

def calculateDistance(point):
    return (point[0] ** 2 + point[1] ** 2) ** .5


if __name__ == "__main__":
    value = [[3,3],[5,-1],[-2,4]]
    import pdb; pdb.set_trace()
    print(kClosest(value,2))
