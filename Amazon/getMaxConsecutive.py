"""
A sliding window approach will work. In order to maximise the number of consecutive 1s, it only makes sense to choose 
adjacent groups of 0s for conversion to 1s (i.e. without any non-chosen 0s between them), otherwise we spend our k on 
creating disjoint islands of 1s, which is a waste. So you'd first choose the first k groups of 0s, then unselect the first one of these and append the next one, 
'...etc, "sliding" through the input, each time checking which one of these options represents the longest result.

e.g:

11101010110011, 2

You flip the first group of 0 and second group of zero which gives you
11111110110011, then that's the longest length, which is 1111111 --> size 7
now disregard the first group and try to move on to see if you flip the next group can make a larger size
so you flip group 1 and 2 you get
11101111110011 --> which is 111111 size 6
flip group 2 and 3 you get
11101011111111 --> 11111111 --> size 8 -> answer is 8
"""
def solve(pattern: str, k: int) -> int:
    start = 0  # start index of the "window"
    size = 0  # Longest result found so far
    import pdb; pdb.set_trace()
    for end in range(len(pattern)):  # Grow window to the right
        if pattern[end] == '0' and (end == 0 or pattern[end - 1] == '1'):
            # We encounter a first '0' in a group of '0's
            k -= 1  # Adjust the number of 0-groups we are still allowed to consume
            if k < 0:  # Must give up a group of '0's
                # Shrink window from the left side, dropping one 0-group
                while pattern[start] == '1':
                    start += 1
                while pattern[start] == '0':
                    start += 1
                k += 1  # ...and allow for one more 0-group at the right

        if end - start >= size:
            size = end + 1 - start  # best so far

    return size





print(solve('11101010110011',1))