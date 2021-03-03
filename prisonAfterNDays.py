def prisonAfterNDays(cells,N):
    return getNewPrison(cells, N)


def getNewPrison(cells, N):
    if N == 0:
        return cells

    copyCells = cells

    for index in range(1, len(cells) - 1):

        beforeCell = index - 1
        nextCell = index + 1
        if cells[beforeCell] == cells[nextCell]:
            copyCells[index] = 1
        else:
            copyCells[index] = 0
    copyCells[len(cells) - 1] = 0
    print(copyCells, N)
    return getNewPrison(copyCells, N - 1)

if __name__ == "__main__":

    import pdb; pdb.set_trace()
    print(prisonAfterNDays([0,1,0,1,1,0,0,1],7))
    a = 1

