def numIslands(grid):
    def helper(row, col):
        grid[row][col] = "0"
        dirs = []
        if row > 0: dirs.append((row - 1, col))
        if row < len(grid) - 1: dirs.append((row + 1, col))
        if col > 0: dirs.append((row, col - 1))
        if col < len(grid[0]) - 1: dirs.append((row, col + 1))

        for d in dirs:
            if grid[d[0]][d[1]] == "1":
                helper(d[0], d[1])
    
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                helper(row, col)
                count += 1
    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
res = numIslands(grid)
print(res)