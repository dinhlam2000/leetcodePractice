"""
The Amazon distribution center consists of arrays of products, each possessing unique attributes. The task at hand is to compute the beauty of these product arrays, with the goal of achieving an efficient selection process.
More specifically, there are arrays of products, and each array corresponds to a list of attributes. The
beauty of a subarray B = [products], products +1],
...,products|r]] is quantified by counting the indices i that satisfy these conditions:
• Isisr
• for every index j such that i < j≤r, products)> productstil
An array Bis a subarray of an array A if B can be obtained from A by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. In particular, an array is a subarray of itself.
The beautiness of the entire array of products is determined by the sum of beauty values across all subarrays of a given size k.

e.g

products = [3,6,2,9,4,1]
k = 3

b = [3,6,2] ... 6 > 2 == 1 , 2 >> next value since it's last value in sub array == 1 ---> 1 + 1 = 2
b = [6,2,9]   9 last value = 1
b = [2,9,4]  9 > 4 > last value = 2
b = [9,4,1] 9 > 4 > 1 > last value = 3
total = 2 + 1 + 2 + 3 = 8
"""
from collections import deque

def find_total_beauty(products, k):
    total_beauty = 0
    dq = deque()

    for index, product in enumerate(products):
        while dq and index - dq[0][1] >= k:
            dq.popleft()

        while dq and dq[-1][0] <= product:
            dq.pop()

        dq.append([product, index])

        if index >= k - 1:
            total_beauty += len(dq)

    return total_beauty


print(find_total_beauty([3,6,2,9,4,1], 3))