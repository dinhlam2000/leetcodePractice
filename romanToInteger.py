def romanToInt(s):
    lookup = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    result = 0
    while char < len(char):
        getTwoString = s[char:char + 2]
        if getTwoString in lookup:
            result = result + lookup[getTwoString]
            char = char + 1
        else:
            result = result + lookup[s[char]]
        char = char + 1
    return result

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    romanToInt("IV")