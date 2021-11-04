# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
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
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(nums, path)
                path.pop()

        result = []
        backtrack(nums, [])
        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]')
    print('Output :')
    print(str(Solution().permute([1, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1]')
    print('Exception :')
    print('[[0,1],[1,0]]')
    print('Output :')
    print(str(Solution().permute([0, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().permute([1])))
    print()

    pass
# @lc main=end
