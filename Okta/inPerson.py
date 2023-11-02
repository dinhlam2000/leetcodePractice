def solution(N,A,B):
    # you can write to stdout for debugging purposes, e.g.
    # print("this is a debug message")
    # write your code in Python 3.6'
    # N attendees
    # relations between attendees are conducted by two array A and B
    # both arrays have length M
    length = len(A)
    result = 0
    relationMapper = {}
    for i in range(N):
        relationMapper[i] = set()
    import pdb; pdb.set_trace()
    for i in range(length):
        a_value = A[i]
        b_value = B[i]
        relationMapper[a_value].add(b_value)
        relationMapper[b_value].add(a_value)
    for key, value in relationMapper.items():
        relationMapper[key] = list(value)
    leaveFlag = list(filter(lambda x: len(x[1]) < 2, relationMapper.items()))
    import pdb; pdb.set_trace()
    while len(leaveFlag) > 0:
        for i in range(len(leaveFlag)):
            value = leaveFlag.pop()
            if len(value[1]) > 0:
                helper(relationMapper, value)
            else:
                del relationMapper[value[0]]
        result = result + 1
        leaveFlag = list(filter(lambda x: len(x[1]) < 2, relationMapper.items()))
    return result

def helper(mapper, value):
    current = value[0]
    neighbors = value[1]
    for neighbor in neighbors:
        mapper[current].remove(neighbor)
        mapper[neighbor].remove(current)
        if len(mapper[current]) == 0:
            del mapper[current]

# n = 7
# a = [0,1,2,1,4,4]
# b = [1,2,0,4,5,6]
# solution(n,a,b)

# n = 7
# a = [0,1,2,4,5]
# b = [1,2,3,5,6]
# solution(n,a,b)

if __name__ == '__main__':
    # z = (100,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])
    # solution(z[0],z[1],z[2])
    N = 100
    a = [i for i in range(0,99)]
    b = [i for i in range(1,100)]
    # print(f'({N},{a},{b})')
    with open('Okta/test.txt', 'w+') as file:
        file.write(f'({N},{a},{b})')