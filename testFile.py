
def read2k() :
    stringReturn = ""
    while len(stringReturn) != 2000:
        stringReturn = stringReturn + "a"
    return stringReturn



def Read(number):
    read2k()
    if number < 0:
        return "Error Value"

    mod = number % 2000
    strReturn = ""
    timeCall = int(number / 2000)
    for i in range(timeCall):
        strReturn = strReturn + read2k()
    if (mod != 0):
        addon = read2k()
        strReturn = strReturn + addon[0:mod]

    return strReturn

if __name__ == "__main__":

    import pdb; pdb.set_trace()
    # for column in range(0, firstLine, 1):
        # for row in range(firstLine - 1, -1, -1):
        #     layer = []
        #     layer.append(matrix[row][column])
        # output.append(layer)
        #
        #


