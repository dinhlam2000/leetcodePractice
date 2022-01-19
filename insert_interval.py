# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

#add all the interval and sort them by the left side then go through each one, then when bar breaks add it, if not then replace the current biggest bar with left lowest and right highest
from typing import List
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    new_list = intervals + [newInterval]

    new_list = sorted(new_list, key=lambda x: x[0])
    print(new_list)
    current = new_list[0]
    result = []
    import pdb; pdb.set_trace()
    for value in new_list[1:]:
        print('', value)
        if value[0] <= current[1]:
            current[0] = min(value[0], current[0])
            current[1] = max(value[1], current[1])
        else:
            result.append(current)
            current = value
    import pdb; pdb.set_trace()
    result.append(current)
    return result

insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])