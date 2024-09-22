import heapq

def min_cost(n, a, b, m):
    # Min-heap to store (price, type, item number)
    heap = []
    
    # Initialize heap with the first item from each type
    for i in range(n):
        heapq.heappush(heap, (a[i], i, 1))  # (price, type index, item number)
    
    total_cost = 0
    print(heap)
    # Extract the smallest m items
    for _ in range(m):
        price, i, j = heapq.heappop(heap)  # Get the smallest price item
        total_cost += price  # Add the price to the total cost
        
        # Insert the next item from the same type (if applicable)
        next_price = a[i] + j * b[i]  # Price of the next item in this type
        heapq.heappush(heap, (next_price, i, j + 1))  # Add the next item to the heap
        print(heap)
    
    return total_cost

# create a heap that's holding the value of (PRICE, i, j) for all items
# we then pop from the heap which will give you the smallest price since the heap will hold its structure that way
# everytime we pop the heap and grab the smallest price, we need to append the next price of that same item onto the heap

def solveMin(n,a,b,m):
    heap = []

    result = 0
    for i in range(n):
        heapq.heappush(heap, (calcPrice(a,b,i,1), i, 1))
    print(heap)
    
    for _ in range(m,0,-1):
        cheapestPrice, i, j = heapq.heappop(heap)
        result = result + cheapestPrice
        nextPrice = calcPrice(a,b,i,j + 1)
        heapq.heappush(heap,(nextPrice, i, j+1))
        print(heap)
    
    return result


def calcPrice(a,b,i,j):
    return a[i] + (j-1)*b[i]







from heapq import heapify, heappush, heappop

# def solve(a,b,m):
#     h = [ (p,q) for p,q in zip(a,b)]
#     print(h)
#     heapify(h)
#     print('heapify', h)
#     res = 0
#     while m:
#         cost, q = heappop(h)
#         res += cost
#         heappush(h, (cost+q,q))
#         m -= 1
#     return res


print(solveMin(3,[2,1,1],[1,2,3],4))
# print(solveMin(3,[2,1,1],[1,2,3],5))

print(min_cost(3,[2,1,1],[1,2,3],4))
# print(min_cost(3,[2,1,1],[1,2,3],5))