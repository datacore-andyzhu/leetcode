# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#


# @lc tags=depth-first-search

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
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start, path):
            if len(path) > 1:
                results.append(path.copy())
            n = len(nums)
            level_set = set()
            for i in range(start,n):
                if (nums[i] in level_set) or \
                    (path and nums[i] < path[-1]):
                    continue
                level_set.add(nums[i])
                path.append(nums[i])
                backtrack(nums, i+1, path)
                path.pop()
        results = []
        backtrack(nums, 0, [])
        return results

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,6,7,7]')
    print('Exception :')
    print('[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]')
    print('Output :')
    print(str(Solution().findSubsequences([4,6,7,7])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [4,4,3,2,1]')
    print('Exception :')
    print('[[4,4]]')
    print('Output :')
    print(str(Solution().findSubsequences([4,4,3,2,1])))
    print()
    
    pass
# @lc main=end