

import json

def get_palindrome(string):
   count = [0]*256
   for i in range(len(string)):
      count[ord(string[i])] += 1
   begin = ""
   mid = ""
   end = ""
   character = ord('a')
   while character <= ord('z'):
      if (count[character] & 1):
         mid = character
         count[character] -= 1
         character -= 1
      else:
         for i in range(count[character]//2):
            begin += chr(character)
      character += 1
   end = begin
   end = end[::-1]
   return begin + chr(mid) + end
def maximalPalindrome(s):
    s = sorted(s)
    og = len(s)
    first = s[0]
    pal = ""
    i = 0
    while len(s) >= 2:
        while s.count(s[0]) > 1:
            pal = pal[:len(pal) // 2] + s[0] + s[1] + pal[len(pal) // 2:]
            if len(s) == 2:
                s = ""
                break
            else:
                s = s[2:]

        s = s[1:]

    if len(pal) != og:
        pal = pal[:len(pal) // 2] + first + pal[len(pal) // 2:]

    return (pal)

if __name__ == "__main__":
    print(get_palindrome('aaabbb'))
    print(maximalPalindrome('aaabbb'))