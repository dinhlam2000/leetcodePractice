# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(B):
    # write your code in Python 3.6

    # B = n x m matrix
    # empty cell = '.'
    # obstacle = 'X'
    # you = 'A'
    # stranger = '< , > , ^ , v' (noting direction sight)
    # stranger can see all the way til first obstacle of other stranger

    # movement can move anywhere from current spot to empty field but no diagonal movement
    # cannot move onto field containing obstacle of other people

    # write a function that you can go from current location to bottom-right cell

    matrix_b = [list(b) for b in B]

    result = False
    # import pdb; pdb.set_trace()
    # import numpy as np
    # print(np.array(matrix_b))
    start_point = [0, 0]
    # mark all the unable to visit cell first
    for i in range(len(matrix_b)):
        for j in range(len(matrix_b[i])):
            if matrix_b[i][j] == '<':
                # matrix_b[i][j] = '#'
                dfs(matrix_b, i, j - 1, 'left')
            elif matrix_b[i][j] == '>':
                # matrix_b[i][j] = '#'
                dfs(matrix_b, i, j + 1, 'right')
            elif matrix_b[i][j] == '^':
                # matrix_b[i][j] = '#'
                dfs(matrix_b, i - 1, j, 'up')
            elif matrix_b[i][j] == 'v':
                # matrix_b[i][j] = '#'
                dfs(matrix_b, i + 1, j, 'down')
            elif matrix_b[i][j] == 'X':
                matrix_b[i][j] = '#'
            elif matrix_b[i][j] == 'A':
                result = True
                start_point = [i, j]
    # import pdb; pdb.set_trace()
    # print(np.array(matrix_b))
    dfs2(matrix_b, start_point[0], start_point[1])
    if result == False:
        return False
    return matrix_b[-1][-1] == 'visited'


def dfs(matrix_b, i, j, direction=None):
    if i < 0 or i >= len(matrix_b) or j < 0 or j >= len(matrix_b[i]):
        return
    if matrix_b[i][j] == '^' or matrix_b[i][j] == '>' or matrix_b[i][j] == '<' or matrix_b[i][j] == 'v':
        return
    if matrix_b[i][j] == 'X':
        matrix_b[i][j] = '#'
        return
    if matrix_b[i][j] == '.' or matrix_b[i][j] == 'A':
        matrix_b[i][j] = '#'
    if direction == 'left':
        dfs(matrix_b, i, j - 1, 'left')
    elif direction == 'right':
        dfs(matrix_b, i, j + 1, 'right')
    elif direction == 'down':
        dfs(matrix_b, i + 1, j, 'down')
    elif direction == 'up':
        dfs(matrix_b, i - 1, j, 'up')


def dfs2(matrix_b, i, j):
    if i < 0 or i >= len(matrix_b) or j < 0 or j >= len(matrix_b[i]):
        return
    if matrix_b[i][j] == '^' or matrix_b[i][j] == '>' or matrix_b[i][j] == '<' or matrix_b[i][j] == 'v':
        return
    if matrix_b[i][j] == '#' or matrix_b[i][j] == 'visited':
        return

    matrix_b[i][j] = 'visited'
    dfs2(matrix_b, i, j - 1)
    dfs2(matrix_b, i, j + 1)
    dfs2(matrix_b, i + 1, j)
    dfs2(matrix_b, i - 1, j)



# print(solution(['.X.', 'XAX', '.X.' ]))
# print(solution(['.<.', '<A>', '...' ]))
# print(solution(['.<.', '<A>', '...' ]))
# print(solution(['<^.', 'vA.']))
# print(solution(['<>.', 'vA.']))
# print(solution(['<^.', 'vAX']))
# print(solution(['<^.', 'vA>']))
# print(solution(['A>.', '...']))
# print(solution(['A..', '.<.']))
# print(solution(['A>.']))
# print(solution(['<A.']))
# print(solution(['<.A']))
# print(solution(['><A']))
# print(solution(['>XA.']))
# print(solution(['><A', '<>.']))
# print(solution(['><.', '<^.', '>^.']))
# print(solution(['A..', '<<.', '>^.']))

test = [['.X.', 'XAX', '.X.' ],
['.<.', '<A>', '...' ],
['.<.', '<A>', '...' ],
['.<.', '<A<', '...' ],
['<^.', 'vA.'],
['<^.', 'vA>'],
['>A.'],
['A..', '<<.', '>^.'],
['><A', '<^.', '>^.'],
['A.']]

for a in test:
    print(solution(a))








