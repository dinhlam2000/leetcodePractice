#make row 1 and column 1 to all be 1
#now add the number before the row and column for that cell
#final cell should be it

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[0] * n] * m
        print(matrix)

        for j in range(n):
            matrix[0][j] = 1

        for i in range(m):
            matrix[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]

