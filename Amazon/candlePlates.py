def platesBetweenCandles(s, queries):
    n = len(s)

    left_candle = [-1] * n
    right_candle = [-1] * n
    prefix_plates = [0] * n

    nearest_left = -1
    for i in range(n):
        if s[i] == '|':
            nearest_left = i
        left_candle[i] = nearest_left
    import pdb; pdb.set_trace()
    
    nearest_right = -1
    for i in range(n-1,-1,-1):
        if s[i] == '|':
            nearest_right = i
        right_candle[i] = nearest_right
    
    plates_count = 0
    for i in range(n):
        if s[i] == '*':
            plates_count += 1
        prefix_plates[i] = plates_count
    
    result = []
    for left , right in queries:
        right_bound = left_candle[right]
        left_bound = right_candle[left]

        if right_bound == -1 or left_bound == -1 or left_bound >= right_bound:
            result.append(0)
        else:
            result.append(prefix_plates[right_bound] - prefix_plates[left_bound])
    import pdb; pdb.set_trace()
    return result

# platesBetweenCandles("**|**|***|",[[0,5],[5,9]])
platesBetweenCandles("*|*|*|",[[0,5]])