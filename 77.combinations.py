# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc tags=backtracking

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
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(n, k, start, path):
            if len(path) == k:
                result.append(path.copy())
                return
            
            for i in range(start, n+1):
                path.append(i)
                backtrack(n, k, i+1, path)
                path.pop()
        result = []
        backtrack(n, k, 1, [])
        
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4, k = 2')
    print('Exception :')
    print('[⁠ [2,4],⁠ [3,4],⁠ [2,3],⁠ [1,2],⁠ [1,3],⁠ [1,4],]')
    print('Output :')
    print(str(Solution().combine(4,2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1, k = 1')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().combine(1,1)))
    print()
    
    pass
# @lc main=end
