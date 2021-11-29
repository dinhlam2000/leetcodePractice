def min_length_substring(s, t):
    # Write your code here
    # t can be empty string? -> return 0
    # s can empty string -> return - 1

    # left and right pointer -> accounts for the windows -> substrings that we're looking at
    ##if that windows contain all the values that appear in t and all values appear in s
    # window's size -> our result

    # left = 0, right = 0 -> right +=
    # incrementing my left: aka. decreasing my window size
    # if new_window is valid: result = len(new_window)
    # if not valid -> incrementing our right

    t_map = {}
    for char in t:
        if char not in t_map:
            t_map[char] = t_map.get(char, 0) + 1

    # t_map => {char : count}
    window_size = -1

    character_covered = 0
    window_map = {}
    left, right = 0, 0
    import pdb;
    pdb.set_trace()

    while right < len(s):

        window_map[s[right]] = window_map.get(s[right], 0) + 1
        if s[right] in t_map and window_map[s[right]] == t_map[s[right]]:
            character_covered += 1

        while left <= right and character_covered == len(t_map):
            window_size = right - left + 1

            # checking if there's a smaller size by incrementing our left up by 1
            char = s[left]
            left = left + 1

            window_map[char] = window_map[char] - 1
            if char not in t_map:
                # decreasing window_size
                window_size = window_size - 1
            else:
                character_covered = character_covered - 1

        right = right + 1

    return window_size


if __name__ == "__main__":
    from collections import Counter

    result = min_length_substring(s = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf", t = "cbccfafebccdccebdd")
    import pdb; pdb.set_trace()
