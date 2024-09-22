"""
string = ceccca
k = 3
output: 7
substring:
cecc --> count 3
ceccc --> count 4
ceccca --> count 4
eccc ---> count 3
eccca --> 3
ccc --> 3
ccca --> 3
"""

def get_k_value(s: str, k: int) -> int:
    # you start counting each character
    # if current character is same as k
    # we know that all the characters after that don't matter
    # and that's the possible solution, is the current substring + x amount of characters left after the current string
    # e.g ceccca
    # substring = cecc -> valid --> cecc _ _ comes after dont matter so the amount up to this point is
    # current + length(s) -  current index 
    result = 0
    start = 0
    char_count = {}
    for i in range(len(s)):
        current_char = s[i]
        char_count[current_char] = char_count.get(current_char,0) + 1
        while char_count[current_char] >= k and start < i:
            start_char = s[start]
            result = result + len(s) - i
            char_count[start_char] = char_count[start_char] - 1
            start = start + 1

    return result

# Example usage:

# Example case with sliding window optimization
user_history = "accada"
k = 2
print(get_k_value(user_history, k))
print(get_k_value('ceccca', 3))
print(get_k_value('acaabbcbc', 3))

