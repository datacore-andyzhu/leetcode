# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#


# @lc tags=array;backtracking

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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """ Solution 1 """
        # nums.sort()
        # n = len(nums)
        # results = []

        # def backtrack(start, k, path):
        #     if len(path) == k and path not in results:
        #         results.append(path[:])
        #         return
        #     for i in range(start, n):
        #         path.append(nums[i])
        #         backtrack(i+1, k, path)
        #         path.pop()
        # for k in range(n+1):
        #     backtrack(0, k, [])
        # return results
        """ Solution 2 """
        def backtrack(nums, start, path):
            results.append(path.copy())
            n = len(nums)
            if start >= n:
                return 
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(nums, i+1, path)
                path.pop()
        results = []
        nums.sort()
        backtrack(nums, 0, [])
        return results
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,2]')
    print('Exception :')
    print('[[],[1],[1,2],[1,2,2],[2],[2,2]]')
    print('Output :')
    print(str(Solution().subsetsWithDup([1, 2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[[],[0]]')
    print('Output :')
    print(str(Solution().subsetsWithDup([0])))
    print()

    pass
# @lc main=end
