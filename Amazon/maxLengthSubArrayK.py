"""
I have an array of size n and am given an integer limit k. 
I have to return the maximum length of a subarray where each element in that subarray exceeds the value of (k / length of that subarray)

"""
def max_length_subarray(arr, cap):
    left = 0
    right = 0
    maxi = 0
    n = len(arr)

    while right < n:
        val = cap / (1.0 * arr[right])
        while left <= right and val > (right - left + 1):
            left += 1
        if left <= right:
            maxi = max(maxi, right - left + 1)
        right += 1

    print("max len of subarray =", maxi)
    return maxi

print(max_length_subarray([2,4,6,8],8))
print(max_length_subarray([10,1,3,8,4],20))