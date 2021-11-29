# Add any helper functions you may need here
def seek(total_day, milestone):
    # binary search to perform this
    # brute force ->> i++
    # 1,5,8,10
    left = 0
    right = len(total_day) - 1
    mid = 0
    first_reached_day = -2
    while left <= right:
        middle = (right + left) // 2
        if total_day[middle] > milestone:
            first_reached_day = middle
            right = middle - 1
        elif total_day[middle] < milestone:
            left = middle + 1
        else:
            return middle + 1
    return first_reached_day + 1


def getMilestoneDays(revenues, milestones):
    # Write your code here
    # milestones are sorted --> not sorted
    # evertyhing will be greater than 0

    # setting our revenue total day by day
    # using that revenue total day by day because it's definitely sorted
    # use binary search in order to find milestones of that current value
    total_day = [0] * len(revenues)
    total_day[0] = revenues[0]
    i = 1
    while i < len(revenues):
        total_day[i] = total_day[i - 1] + revenues[i]
        i += 1
    print(revenues, total_day, milestones)

    result = [-1] * len(milestones)

    for index, milestone in enumerate(milestones):
        import pdb; pdb.set_trace()
        day = seek(total_day, milestone)
        result[index] = day

    return result


print(getMilestoneDays( [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100,200,500]))
