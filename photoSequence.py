def photoSequence(n,index,identity):
    # create a hash map with key and mapping to value
    # and everytime a key is inserted, and that key already existed in the hash map, increment that

    result = []

    indexValueMap = {}

    for i in range(len(index)):
        position = index[i]
        if position not in indexValueMap:
            indexValueMap[position] = identity[i]
        else:
            # find all the position above it and shift it up by one
            for newPosition in range(position,position +len(indexValueMap) - position):


