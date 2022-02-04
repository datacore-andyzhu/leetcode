# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#


# @lc tags=dynamic-programming

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
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if stones[1] != 1:
            return False
        dp = [[False for _ in range(n)] for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                k = stones[i] - stones[j]
                if k > j+1:
                    break
                dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]

                if i == n-1 and dp[i][k]:
                    return True
        return False
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('stones = [0,1,3,5,6,8,12,17]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canCross([0,1,3,5,6,8,12,17])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('stones = [0,1,2,3,4,8,9,11]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canCross([0,1,2,3,4,8,9,11])))
    print()
    
    pass
# @lc main=end
