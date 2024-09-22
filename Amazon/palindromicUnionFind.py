class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

def min_operations_to_palindrome(arr):
    n = len(arr)
    if n <= 1:
        return 0
    
    # Create a union-find structure for the unique values in the array
    unique_values = {value: i for i, value in enumerate(set(arr))}
    uf = UnionFind(len(unique_values))

    # Union the pairs of elements that need to be the same
    for i in range(n // 2):
        left_value = arr[i]
        right_value = arr[n - 1 - i]
        if left_value != right_value:
            uf.union(unique_values[left_value], unique_values[right_value])
    
    # Count unique roots (groups)
    root_set = set()
    for value in arr:
        root_set.add(uf.find(unique_values[value]))

    # The number of operations is the number of unique groups minus 1
    import pdb; pdb.set_trace()
    return len(uf.parent) - len(root_set) 

# Example usage:
arr1 = [1, 2, 3, 4, 3, 2, 1]
print(min_operations_to_palindrome(arr1))  # Output: 0 (already palindromic)

arr2 = [1, 2, 3, 4, 5]
print(min_operations_to_palindrome(arr2))  # Output: 2


# Example usage:
arr1 = [1, 2, 3, 4, 3, 2, 1]
print(min_operations_to_palindrome(arr1))  # Output: 0 (already palindromic)


arr2 = [1, 1, 3, 4, 5] # --> 5,5,3,4,5
# {1,4,5} {3} 
# >>
print(min_operations_to_palindrome(arr2))  # Output: 2
