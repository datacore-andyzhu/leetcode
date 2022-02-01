# @lc app=leetcode id=765 lang=python3
#
# [765] Couples Holding Hands
#


# @lc tags=tree

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
class Solution:
    """ Solution 1: Union Set"""
    def __init__(self):
        self.pairs = [-1] * 70

    def find(self, x):
        if x != self.pairs[x]:
            self.pairs[x] = self.find(self.pairs[x])
        return self.pairs[x]

    def union(self, x, y):
        self.pairs[self.find(x)] = self.pairs[self.find(y)]

    def minSwapsCouples(self, row: List[int]) -> int:
        persons = len(row)
        couples = persons // 2
        for i in range(couples):
            self.pairs[i] = i
        for i in range(0, persons, 2):
            self.union(row[i]//2, row[i+1]//2)
        count = 0
        for i in range(couples):
            if i == self.find(i):
                count += 1
        return couples - count
    """ Solution 2: Greedy Method """

    # def minSwapsCouples(self, row: List[int]) -> int:
    #     n = len(row)
    #     ans = 0
    #     cache = [0] * n
    #     for i in range(n):
    #         cache[row[i]] = i
    #     for i in range(0, i-1, 2):
    #         a = row[i]
    #         b = a ^ 1
    #         if row[i+1] != b:
    #             src = i + 1
    #             tgt = cache[b]
    #             cache[row[tgt]] = src
    #             cache[row[src]] = tgt
    #             row[src], row[tgt] = row[tgt], row[src]
    #             ans += 1
    #     return ans
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('row = [0,2,1,3]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minSwapsCouples([0,2,1,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('row = [3,2,0,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minSwapsCouples([3,2,0,1])))
    print()
    
    pass
# @lc main=end
