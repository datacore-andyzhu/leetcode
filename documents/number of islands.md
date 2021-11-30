#### [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'



**解题思路**

**深度优先搜索**：求连通块的个数
	每次深搜可以遍历图中的一个连通块，所以，深搜的次数就是连通块的个数
	每访问一个为"1"的位置，将其替换为"0"，代替visited数组标记节点是否被访问过
	同理，使用广度优先搜索，搜索的次数就是连通块的个数，即岛屿的数量
**并查集**
	初始化每个位置为一个集合，用i*col+j唯一标识每个元素
	初始化size=col*row
	合并连通的元素为一个集合，每合并一次，size-1
	最终size = 连通块的个数 + 水的元素个数
	故在遍历每个元素的时候，统计水的个数
	岛屿数量 = size - 水的个数

**代码**
**深度优先搜索**

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 深度优先搜索：
        def dfs(i, j):
            grid[i][j] = '0'

            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x>=0 and x<n and y>=0 and y<m and grid[x][y]=='1':
                    dfs(x, y)

        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                # 深搜的次数就是岛屿的个数
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res


```
**广度优先搜索**

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 深度优先搜索：
        def bfs(i, j):
            queue = [(i, j)]
            grid[i][j] = "0"
            while queue:
                x, y = queue.pop(0)
                for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if a>=0 and a<n and b>=0 and b<m and grid[a][b]=="1":
                        queue.append((a, b))
                        grid[a][b] = "0"

        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)

        return res

```
**并查集**

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 并查集：使用横坐标*列数+纵坐标作为元素在并查集中的唯一标识
        # 岛屿数量 = （总元素个数 - 水的个数）中的连通块的个数
        class UnionFind:
            def __init__(self, n):
                # 总数
                self.size = n
                self.p = [i for i in range(n)]

            def find(self, x):
                # 查找根节点，即当前元素所属的集合
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, a, b):
                
                ar, br = self.find(a), self.find(b)
                # 两个元素位于同一个集合，跳过
                if ar == br:
                    return
                # 不在同一个集合，合并
                else:
                    self.p[ar] = br 
                    self.size -= 1

        n, m = len(grid), len(grid[0])
        ocean = 0   # 统计水的个数

        uf = UnionFind(n*m)

        for i in range(n):
            for j in range(m):
                # 统计水的个数
                if grid[i][j] == "0":
                    ocean += 1
                else:
                    # 只需向右和向下查看
                    if i+1 < n and grid[i+1][j]=="1":
                        uf.union(i*m+j, (i+1)*m+j)
                    if j+1 < m and grid[i][j+1]=="1":
                        uf.union(i*m+j, i*m+(j+1))
                
        return uf.size - ocean
```

