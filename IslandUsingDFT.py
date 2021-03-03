#using DFT to find the number of island on the map
#have a visited array that is the same size of the original array
#keep track of which node is visited
#start with upper left and keep searching
#if it's a zero mark as visited immediately
#perform the dfs on values that are one
#everytikme we perform dfs we increment island number by 1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numberIsland = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    grid[i][j] = "visit"
                elif grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    numberIsland += 1
        return numberIsland

    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return
        if grid[i][j] == "0":
            grid[i][j] = "visit"
            return
        if grid[i][j] == "visit":
            return
        grid[i][j] = "visit"

        self.dfs(i + 1, j, grid)
        self.dfs(i - 1, j, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i, j - 1, grid)


if __name__ == "__main__":
    input1 = [
        ["1", "1", "0", "0", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "0", "0", "1", "1"]
]
    sorted()
    import pdb; pdb.set_trace()
    print(numIslands(input1))
