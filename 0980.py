def uniquePathsIII(grid):
    row_count = len(grid)
    col_count = len(grid[0])
    def helper(grid, pos, left):
        if grid[pos[0]][pos[1]] == 2 and left == 0:
            return 1
        grid = [i[:] for i in grid]
        grid[pos[0]][pos[1]] = 1
        temp_count = 0
        if pos[0] < row_count - 1 and (grid[pos[0] + 1][pos[1]] == 0 or grid[pos[0] + 1][pos[1]] == 2):
            temp_count += helper(grid, (pos[0] + 1, pos[1]), left - 1)
        if pos[0] > 0 and (grid[pos[0] - 1][pos[1]] == 0 or grid[pos[0] - 1][pos[1]] == 2):
            temp_count += helper(grid, (pos[0] - 1, pos[1]), left - 1)
        if pos[1] < col_count - 1 and (grid[pos[0]][pos[1] + 1] == 0 or grid[pos[0]][pos[1] + 1] == 2):
            temp_count += helper(grid, (pos[0], pos[1] + 1), left - 1)
        if pos[1] > 0 and (grid[pos[0]][pos[1] - 1] == 0 or grid[pos[0]][pos[1] - 1] == 2):
            temp_count += helper(grid, (pos[0], pos[1] - 1), left - 1)
        return temp_count
    
    open_count = 1
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            open_count += col == 0
            if col == 1:
                start_pos = (r, c)
    
    return helper(grid, start_pos, open_count)

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
res = uniquePathsIII(grid)
print(res)