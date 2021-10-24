def segmentsCovering(segments):
    if len(segments) == 1:
        return 1
    sorted_segment = sorted(segments, key=lambda x: x[1])
    print(sorted_segment)
    result = 1
    start_point = sorted_segment[0][1]
    for segment in sorted_segment[1:]:
        if segment[0] > start_point:
            result = result + 1
            start_point = segment[1]

    return result


def addToPoints(value, result):
    for i in range(value[0], value[1] + 1):
        result.append(i)
    return result

if __name__ == '__main__':
    input_segments = [
        [-1,3],
        [-5,5],
        [3,5],
        [2,4],
        [-3,3],
        [-1,4],
        [5,5]
    ]
    print(segmentsCovering(input_segments))