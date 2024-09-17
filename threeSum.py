f#iterate through the list
#get the next value and last value
#then check the sum of all three numbers
#if it's greater than 0 then decrease right, else left
#if it's 0 then you append the three values and incremet left
def threeSum(nums):


    nums.sort()
    triplet = []
    for index, value in enumerate(nums):
        left = index + 1
        right = len(nums) - 1
        while left < right:
            threeSum = nums[left] + nums[right] + value
            if threeSum == 0:
                triplet.append([value ,nums[left] ,nums[right]])
                left = left + 1
                while nums[left] == nums[left - 1] and left < right:
                    left = left + 1
            elif threeSum < 0:
                left = left + 1
            else:
                right = right - 1


    return triplet