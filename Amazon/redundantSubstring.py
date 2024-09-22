def is_vowel(ch):
    return ch in 'aeiouAEIOU'

def count_redundant_substrings(word, a, b):
    n = len(word)
    redundant_count = 0
    
    # Precompute number of vowels and consonants up to each index
    vowel_count = [0] * (n + 1)
    consonant_count = [0] * (n + 1)
    
    for i in range(1, n + 1):
        vowel_count[i] = vowel_count[i - 1] + (1 if is_vowel(word[i - 1]) else 0)
        consonant_count[i] = consonant_count[i - 1] + (1 if not is_vowel(word[i - 1]) else 0)
    
    print(word)
    print(vowel_count)
    print(consonant_count)
    # Iterate over all substrings
    for start in range(n):
        for end in range(start + 1, n + 1):
            # Calculate number of vowels and consonants in substring word[start:end]
            v = vowel_count[end] - vowel_count[start]
            c = consonant_count[end] - consonant_count[start]
            
            # Calculate the length of the substring
            length = end - start
            
            # Check if it satisfies the condition |substring| = a*v + b*c
            if length == a * v + b * c:
                redundant_count += 1
                
    return redundant_count

def is_vowel(c):
    return c in 'aeiuoAEIUO'
def count_redundant(word,a,b):
    n = len(word)
    # Precompute number of vowels and consonants up to each index
    vowel_word = [0]*(n+1)
    consonant_word = [0]*(n+1)
    for i in range(1,n+1):
        if is_vowel(word[i-1]):
            vowel_word[i] = vowel_word[i-1] + 1
            consonant_word[i] = consonant_word[i-1]
        else:
            vowel_word[i] = vowel_word[i-1]
            consonant_word[i] = consonant_word[i-1] + 1
    print(word)
    print(vowel_word)
    print(consonant_word)
    redundant = 0

    # for each substring we go through, get the number of vowels + number of consonant
    for start in range(n):
        for end in range(start+1,n + 1):
            # substring is word[start:end]
            print('substring', word[start:end])
            number_vowel = vowel_word[end] - vowel_word[start]
            number_consonant = consonant_word[end] - consonant_word[start]
            length_word = end - start
            if length_word == number_vowel*a + number_consonant*b:
                redundant += 1
    return redundant


# Example usage
word = "abbacc"
a = -1
b = 2

word2 = "akljfs"
a2 = -2
b2 = 1

word3 = "afejipl"
a3 = 4
b3 = -2
print(count_redundant(word, a, b))  # Output: The number of redundant substrings
print(count_redundant(word2, a2, b2))  # Output: The number of redundant substrings

print(count_redundant(word3, a3, b3))  # Output: The number of redundant substrings


