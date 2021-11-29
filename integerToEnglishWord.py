class Solution:
    def __init__(self):
        self.sub10 = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
        }
        self.post10 = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety',
        }
        self.teens = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
        }

    def numberToWords(self, num: int, recursive=False) -> str:
        import pdb; pdb.set_trace()
        if not num:
            return 'Zero' if not recursive else ''
        if num >= 1000000000:
            result = self.numberToWords(num // 1000000000, True) + ' Billion ' + self.numberToWords(num % 1000000000,
                                                                                                    True)
        if num >= 1000000 and num < 1000000000:
            result = self.numberToWords(num // 1000000, True) + ' Million ' + self.numberToWords(num % 1000000, True)
        if num >= 1000 and num < 1000000:
            result = self.numberToWords(num // 1000, True) + ' Thousand ' + self.numberToWords(num % 1000, True)
        if num >= 100 and num < 1000:
            result = self.sub10[num // 100] + ' Hundred ' + self.numberToWords(num % 100, True)
        elif num >= 20 and num < 100:
            result = self.post10[num // 10] + ' ' + self.numberToWords(num % 10, True)
        elif num >= 10 and num < 20:
            result = self.teens[num]
        elif num < 10:
            result = self.sub10[num]
        return result.strip()

print(Solution().numberToWords(1234))