def solve(s: str, k: int) -> int:
    ans = 0
    n = len(s)
    
    for i in range(n - k + 1):
        left = i
        right = i + k - 1
        if s[right] < s[left]:
                ans += 1
        # while left < right:
        #     if s[right] < s[left]:
        #         ans += 1
        #         break
        #     left += 1
        #     right -= 1
            
    return ans


print(solve('acebd', 4))
print(solve('abcde',2))
print(solve('edcba', 3))
print(solve('amazon',3))