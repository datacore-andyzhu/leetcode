def numDistinctIslands(grid):

    def dfs(grid, x, y, dir):
        nonlocal string
        m = len(grid)
        n = len(grid[0])

        if x < 0 or x >=m or y <0 or y >= n:
            return 
        if grid[x][y] == 0:
            return

        grid[x][y] = 0
        string = string + dir + '.'
        dfs(grid, x+1, y, '1')
        dfs(grid, x-1, y, '2')
        dfs(grid, x, y+1, '3')
        dfs(grid, x, y-1, '4')
        string = string + '-' + dir + '.'

    islands = set()
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                string = ''
                dfs(grid, i, j, '0')
                islands.add(string)
    
    return len(islands)
