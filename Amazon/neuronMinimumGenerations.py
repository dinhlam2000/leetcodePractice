"""
An ml model has a certain array of neurons, in each odd generation a neuron can be increased by 1, in even generations it can be increased by 2.

 Output: Return min generations to make all neurons equal.

Eg: {1,1,2,4} → generation1 {2,1,2,4} → generation2 {4,1,2,4} → generation3 {4,2,2,4} → generation4 {4,4,2,4} → generation5 (no change) → generation6 {4,4,4,4}
"""
def solve(neurons):
    max_val = max(neurons)
    one, two = 0, 0
    for v in neurons:
        v = max_val - v
        if v % 2 == 1:
            one += 1 # Count how many are odd (1s in binary)
        two += v // 2  # Count how many can be halved

    def best(one, two):
        if one > two:
            return one * 2 - 1
        move = (two - one) // 3
        two -= move
        one += move * 2
        return one + two + (0 if one == two else 1)

    return min(best(one, two), best(len(neurons) - one, one + two))

# Example usage:
neurons = [1, 2, 2, 3] # 1,3,2,3    3,3,2,3     3,3,3,3   --> 3
neurons2 = [1,1,2,4] # 2,1,2,4   4,1,2,4   4,2,2,4   4,4,2,4  4,4,2,4   4,4,4,4  --> 6
neurons3 = [1,1,2,3]  # 1,1,3,3  3,1,3,3   3,1,3,3     3,3,3,3  -> 4
print(solve(neurons))  # Output: 3
print(solve(neurons2)) # output = 6
print(solve(neurons3)) # output -> 4

