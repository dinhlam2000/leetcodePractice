def number_to_words(num):
    # fill in this method
    sub_tenth = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
        }
    sub_twenty = {
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen"
    }
    ty_map = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety"
    }
    result = []
    def helper(n, recursive=True):
        if n == 0:
            result.append("Zero") if not recursive else ""

        elif n >= 1000000000:
            helper(n//1000000000)
            result.append("Billion")
            helper(n%1000000000)
        elif n >= 1000000:
            helper(n//1000000)
            result.append("Million")
            helper(n%1000000)
        elif n >= 1000:
            helper(n//1000)
            result.append("Thousand")
            helper(n%1000)
        elif n >= 100:
            helper(n//100)
            result.append("Hundred")
            helper(n%100)
        elif n >= 20:
            result.append(ty_map[n//10])
            helper(n%10)
        elif n > 10:
            result.append(sub_twenty[n])
        elif n >= 0:
            result.append(sub_tenth[n])
    helper(num,recursive=False)
    result.insert(len(result) - 2, 'and')
    return " ".join(result).lower()