# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#


# @lc tags=string;heap;greedy;sort

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.size = n

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

    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        edges = list()
        for i in range(n):
            for j in range(n):
                idx = i*n+j
                if i > 0:
                    edges.append((idx-n, idx, max(grid[i][j], grid[i-1][j])))
                if j > 0:
                    edges.append((idx-1, idx, max(grid[i][j], grid[i][j-1])))
        
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n*n)
        ans = -1
        for x, y, v in edges:
            uf.union(x, y)
            ans = max(ans, v)
            if uf.connected(0, n*n-1):
                return ans
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,2],[1,3]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().swimInWater([[0,2],[1,3]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('grid =[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]')
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])))
    print()
    
    pass
# @lc main=end
