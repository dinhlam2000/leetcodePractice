"""
Q. sum of k should be less than or equal to threshold. Question was to find number of elements that should be removed to make sum of any
k elements in array less than threshold.

SOLUTION:
Sort the array of prices in descending order, HIGHEST ---> LOWEST

Grab the first k items -->
if sum <= threshold of k items, then return result since we know that these are the highest items, meaning any other possible combinations will be less
since this is the max
if sum > threshold, then we remove the top value

e.g -> 9, 6, 7, 2 ,7 ,2 --> [9,7,7,6,2,2] THRESHOLD is 13, k = 2

"""
def reduceGifts(prices,k,threshold):
    prices = sorted(prices, reverse=True)
    result = 0
    i = 0
    while i <= len(prices) - k:
        currentGreatestSum = sum(prices[i:i+k])
        if currentGreatestSum <= threshold:
            break
        
        i = i + 1
        result = result + 1

    return result

# print(reduceGifts([1,8,4,5], 2, 10))
# print(reduceGifts([4,5,1,9,1], 2, 10))
# print(reduceGifts( [3, 2, 1, 4, 6, 5], 3, 14))
# print(reduceGifts([10, 20, 30, 40, 50], 3, 60))
# print(reduceGifts([9,6,7,2,7,2], 2, 13))
# print(reduceGifts([10, 20, 30, 40, 50], 3, 90))
# print(reduceGifts([60], 1, 50))
# print(reduceGifts([100,200,300,400], 1, 50))
# print(reduceGifts([5,10,15], 2, 30))

prices = [i for i in range(1, 1001)]  # List from 1 to 1000
k = 5
threshold = 2000
print(reduceGifts(prices,k,threshold))




