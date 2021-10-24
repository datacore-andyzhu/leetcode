# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#


# @lc tags=Unknown

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
    def __init__(self, n) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
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

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # create an unionfind
        # link all the node together accordign to 
        # the relation defind in the pairs
        n = len(s)
        uf = UnionFind(n)
        for pair in pairs:
            uf.union(pair[0], pair[1])

        # create a adjacent list by using the union find structure
        # this way, we know each char in the string s's parent
        graph = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            graph[root].append(s[i])
        
        # sort the adjacent list by reverse order of alphabet, so we know 
        # for the char in s, what is the minimum order of char is
        for arr in graph.values():
            arr.sort(reverse=True)
        
        # then we just replace each char's root's minimum lexicographically char
        arr = ['.'] * n
        for i in range(n):
            parent = uf.find(i)
            arr[i] = graph[parent].pop()

        return ''.join(arr)
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "dcab", pairs = [[0,3],[1,2]]')
    print('Exception :')
    print('"bacd"Explaination:Swap s[0] and s[3], s = "bcad"Swap s[1] and s[2], s = "bacd"')
    print('Output :')
    print(str(Solution().smallestStringWithSwaps("dcab",[[0,3],[1,2]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "dcab", pairs = [[0,3],[1,2],[0,2]]')
    print('Exception :')
    print('"abcd"Explaination:Swap s[0] and s[3], s = "bcad"Swap s[0] and s[2], s = "acbd"Swap s[1] and s[2], s = "abcd"')
    print('Output :')
    print(str(Solution().smallestStringWithSwaps("dcab",[[0,3],[1,2],[0,2]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "cba", pairs = [[0,1],[1,2]]')
    print('Exception :')
    print('"abc"Explaination:Swap s[0] and s[1], s = "bca"Swap s[1] and s[2], s = "bac"Swap s[0] and s[1], s = "abc"')
    print('Output :')
    print(str(Solution().smallestStringWithSwaps("cba",[[0,1],[1,2]])))
    print()
    
    pass
# @lc main=end