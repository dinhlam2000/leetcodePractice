# class Solution:
#     def __init__(self):
#         self.sub10 = {
#             1: 'One',
#             2: 'Two',
#             3: 'Three',
#             4: 'Four',
#             5: 'Five',
#             6: 'Six',
#             7: 'Seven',
#             8: 'Eight',
#             9: 'Nine',
#         }
#         self.post10 = {
#             2: 'Twenty',
#             3: 'Thirty',
#             4: 'Forty',
#             5: 'Fifty',
#             6: 'Sixty',
#             7: 'Seventy',
#             8: 'Eighty',
#             9: 'Ninety',
#         }
#         self.teens = {
#             10: 'Ten',
#             11: 'Eleven',
#             12: 'Twelve',
#             13: 'Thirteen',
#             14: 'Fourteen',
#             15: 'Fifteen',
#             16: 'Sixteen',
#             17: 'Seventeen',
#             18: 'Eighteen',
#             19: 'Nineteen',
#         }
#
#     def numberToWords(self, num: int, recursive=False) -> str:
#         if not num:
#             import pdb; pdb.set_trace()
#             return 'Zero' if not recursive else ''
#         if num >= 1000000000:
#             result = self.numberToWords(num // 1000000000, True) + ' Billion ' + self.numberToWords(num % 1000000000,
#                                                                                                     True)
#         if num >= 1000000 and num < 1000000000:
#             result = self.numberToWords(num // 1000000, True) + ' Million ' + self.numberToWords(num % 1000000, True)
#         if num >= 1000 and num < 1000000:
#             result = self.numberToWords(num // 1000, True) + ' Thousand ' + self.numberToWords(num % 1000, True)
#         if num >= 100 and num < 1000:
#             result = self.sub10[num // 100] + ' Hundred ' + self.numberToWords(num % 100, True)
#         elif num >= 20 and num < 100:
#             result = self.post10[num // 10] + ' ' + self.numberToWords(num % 10, True)
#         elif num >= 10 and num < 20:
#             result = self.teens[num]
#         elif num < 10:
#             result = self.sub10[num]
#         return result.strip()
#
# print(Solution().numberToWords(1234))

class Solution:
    def numberToWords(self, num: int) -> str:

        result = ""
        result = self.helper(num, result)
        return result

    def helper(self, num: int, word: str, recursive=False) -> str:
        sub_ten = {1: 'One',
                   2: 'Two',
                   3: 'Three',
                   4: 'Four',
                   5: 'Five',
                   6: 'Six',
                   7: 'Seven',
                   8: 'Eight',
                   9: 'Nine',
                   10: 'Ten'
                   }
        sub_twenty = {11: 'Eleven',
                      12: 'Twelve',
                      13: 'Thirteen',
                      14: 'Fourteen',
                      15: 'Fifteen',
                      16: 'Sixteen',
                      17: 'Seventeen',
                      18: 'Eighteen',
                      19: 'Nineteen'
                      }
        ty_map = {2: 'Twenty',
                  3: 'Thirty',
                  4: 'Fourty',
                  5: 'Fifty',
                  6: 'Sixty',
                  7: 'Seventy',
                  8: 'Eighty',
                  9: 'Ninety'
                  }
        if not num:
            return 'Zero' if not recursive else ''
        if num >= 1000000000:
            word = word + self.helper(num // 1000000000, True) + ' Billion' + self.helper(num % 1000000000, True)
        elif num >= 1000000:
            word = word + self.helper(num // 1000000, True) + ' Million' + self.helper(num % 1000000, True)
        elif num >= 1000:
            word = word + self.helper(num // 1000, True) + ' Thousand' + self.helper(num % 1000, True)
        elif num >= 100:
            word = word + self.helper(num // 100, True) + ' Hundred' + self.helper(num % 100, True)
        elif num >= 20:
            word = word + ty_map[num // 10] + self.helper(num % 10, True)
        elif num > 10:
            word = word + sub_twenty[num]
        elif num >= 0:
            word = word + sub_ten[num]
        return word

print(Solution().numberToWords(1234))