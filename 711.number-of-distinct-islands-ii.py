def numDistinctIslands2(grid):
    # https://massivealgorithms.blogspot.com/2018/12/leetcode-711-number-of-distinct-islands.html
    def dfs(grid, x, y):
        nonlocal cells 
        m = len(grid)
        n = len(grid[0])
        if x < 0 or x >=m or y < 0 or y >= n:
            return
        if grid[x][y] == 0:
            return
        cells.append((x, y))
        grid[x][y] = 0
        dfs(grid, x+1, y)
        dfs(grid, x-1, y)
        dfs(grid, x, y+1)
        dfs(grid, x, y-1)
    
    def getKey(cells):
        cells.sort(key=lambda x:(x[0], x[1]))

        key = []
        originX = cells[0][0]
        originY = cells[0][1]
        for cell in cells:
            key.append(str(cell[0]-originX) + ':' + str(cell[1]-originY))
        return ''.join(key)


    def cellsTransform(cells):
        transformations = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        forms = []
        for tran in transformations:
            list1 = []
            list2 = []
            for cell in cells:
                x = cell[0]
                y = cell[1]
                # generate the 8 different transformations
                # (x, y), (x, -y), (-x, y), (-x, -y)
                # (y, x), (-y, x), (y, -x), (-y, -x)
                list1.append(x*tran[0], y*tran[1])
                list2.append(y*tran[1], x*tran[0])
            forms.append(getKey(list1))
            forms.append(getKey(list2))
        
        forms.sort()
        return forms[0]
        

    if grid is None or len(grid) == 0:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    islands = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                cells = []
                dfs(grid, i, j)
                key = cellsTransform(cells)
                islands.add(key)
    return len(islands)

