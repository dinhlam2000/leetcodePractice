
def matching_pairs(s, t):
    # Write your code here

    # edge case 1:
    # s == t
    # CHECK IF WE HAVE DUPLICATE
    # if there is duplicate then, return len(s)
    # if no duplicaten, return len(s) - 2

    if s == t:
        if len(set(s)) < len(s):
            return len(s)
        return len(s) - 2

    count = 0
    i = 0
    unmatch_s = set()
    unmatch_t = set()
    unmatch_pair_s_t = set()
    perfect_swap = False
    half_swap = False
    print(s ,t)
    while i < len(s):
        if s[i] != t[i]:
            unmatch_pair_s_t.add((s[i] ,t[i]))
            unmatch_s.add(s[i])
            unmatch_t.add(t[i])
            if (t[i], s[i]) in unmatch_pair_s_t:
                perfect_swap = True
                i += 1
                continue
            if t[i] in unmatch_s or s[i] in unmatch_t:
                half_swap = True
        else:
            count = count + 1
        i += 1

    if perfect_swap == True:
        return count + 2
    if half_swap == True:
        return count + 1
    return count

    # iterate each character -> s[i] and t[i]
    # if they match we dont do anything
    # if they dont match --> add s[i] to unmatch_set_s, add t[i] to unmatch_set_t

    # perform swap positive: total_count + 2 or total_count + 1 or total_count
    # perform swap negative: total_count total_count - 2

    # perfect_swap = false
    # half_swap = false

