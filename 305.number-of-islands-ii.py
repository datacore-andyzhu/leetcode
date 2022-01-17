class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        class DSU:
            def __init__(self, length) -> None:
                self.root = [i for i in range(length)]
                self.island = [False] * length
                self.rank = [1] * length
                self.count = 0
            
            def find(self, x):
                if x == self.root[x]:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootY] > self.rank[rootX]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1
                    self.count -= 1
            def addLand(self, x):
                self.island[x] = True
                self.count += 1
        def index(x, y):
            return x*n+y
        
        dsu = DSU(m*n)
        res = []
        for position in positions:
            x, y = position[0], position[1]
            dsu.addLand(index(x, y))
            if x -1 >= 0 and dsu.island(index(x-1, y)):
                dsu.union(index(x, y), index(x-1, y))
            if x + 1< m and dsu.island(index(x+1, y)):
                dsu.union(index(x, y), index(x+1, y))
            if y - 1 >= 0 and dsu.island(index(x, y-1)):
                dsu.union(index(x, y), index(x, y-1))
            if y+1 < m and dsu.island(index(x, y+1)):
                dsu.union(index(x, y), index(x, y+1))
            res.append(dsu.count)
        
        return res
