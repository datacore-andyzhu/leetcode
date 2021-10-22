# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#


# @lc tags=depth-first-search;union-find

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
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1 for x in range(size)]
        # Initially each item is a province itself
        self.count = size
    
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
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
    def conncted(self, x, y):
        return self.find(x) == self.find(y)

    def getCount(self):
        return self.count
    

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        provinces = UnionFind(n)
        for row in range(n):
            for col in range(row+1, n):
                if isConnected[row][col] == 1:
                    provinces.union(row, col)
        return provinces.count
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('isConnected = [[1,1,0],[1,1,0],[0,0,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('isConnected = [[1,0,0],[0,1,0],[0,0,1]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])))
    print()
    
    pass
# @lc main=end
