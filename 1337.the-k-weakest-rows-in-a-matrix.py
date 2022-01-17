# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#


# @lc tags=Unknown

# @lc imports=start
from imports import *
import heapq
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
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """ Solution 1 """
        # result = []
        # low_strength = []
        # for i in range(len(mat)):
        #     low_strength.append((sum(mat[i]),i))
        # low_strength.sort(key=lambda x:(x[0], x[1]))
        # for i in range(k):
        #     result.append(low_strength[i][1])
        # return result
        """ Solution 2: """
        m = len(mat)
        n = len(mat[0])
        positions = []
        for i in range(m):
            left = 0
            right = n-1
            pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if mat[i][mid] == 0:
                    right = mid - 1
                else:
                    pos = mid
                    left = mid + 1
            positions.append((pos+1, i))
        heapq.heapify(positions)
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(positions)[1])
        return ans
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('mat =[[1,1,0,0,0],⁠[1,1,1,1,0],⁠[1,0,0,0,0],⁠[1,1,0,0,0],⁠[1,1,1,1,1]],k = 3')
    print('Exception :')
    print('[2,0,3]')
    print('Output :')
    print(str(Solution().kWeakestRows([[1,1,0,0,0],⁠[1,1,1,1,0],⁠[1,0,0,0,0],⁠[1,1,0,0,0],⁠[1,1,1,1,1]],3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('mat =[[1,0,0,0],⁠[1,1,1,1],⁠[1,0,0,0],⁠[1,0,0,0]],k = 2')
    print('Exception :')
    print('[0,2]')
    print('Output :')
    print(str(Solution().kWeakestRows([[1,0,0,0],⁠[1,1,1,1],⁠[1,0,0,0],⁠[1,0,0,0]],2)))
    print()
    
    pass
# @lc main=end
