def kClosest(points,K):
    mapDistancePoint = {}  # key is distance, value is just the point

    for value in points:
        distance = (value[0] ** 2 + value[1] ** 2) ** (0.5)
        distance = round(distance, 2)
        if distance not in mapDistancePoint:
            mapDistancePoint[distance] = []
            mapDistancePoint[distance].append(value)
        else:
            mapDistancePoint[distance].append(value)

    # have a map of distance --> point

    sortedKey = sorted(mapDistancePoint.items(), key=lambda x: (x[0], x[1]))

    # sortedKey with the point

    result = []
    for i in range(K):
        while len(sortedKey[i][1]) != 0:
            value = sortedKey[i][1].pop(0)
            result.append(value)
    return result


if __name__ == "__main__":
    value = [[0, 1], [1, 0]]
    import pdb; pdb.set_trace()
    print(kClosest(value,1))
