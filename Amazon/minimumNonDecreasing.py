"""
Find the max value
find the idfference by using max value - current number
current number will be nums[i] + result
if diff is > 0>, that means this is now decreasing, so we have to add to result by diff
"""
def calc(nums):
    max_value = nums[0]
    result = 0
    for i in range(1,(len(nums))):
          current = nums[i] + result
          diff = max_value - current
          if diff > 0: result = result + diff
          max_value = max(max_value,current)
    return result
    

cases = [[3, 4, 1, 6, 2], [3, 2, 1], [4, 4, 4, 8], [1, 2, 3, 4], [4, 3, 2, 1], [4, 3, 2, 1, 8, 9, 10, 1, 2, 3]]
for i in cases:
	print(i, calc(i))

print(calc([3,4,1,6,2]))
print(calc([3,2,1]))
print(calc([4, 3, 2, 1, 8, 9, 10, 1, 2, 3]))