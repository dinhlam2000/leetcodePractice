#go through the matrix 1 by 1
#everytime you hit a 1 then perform a dfs and increase island counter by 1
#also mark it as visit
#if you hit a 0 you mark it visit immediately
#if it's visit you dont do shit and just return
#if it's 0 when you're performing dfs you mark it as visit return
#hit a one then perform top bottom left right
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
