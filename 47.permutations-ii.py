# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#


# @lc tags=backtracking

# @lc imports=start
import collections
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
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_dict = collections.Counter(nums)
        results = []

        def backtrack(path, nums_dict):
            if len(path) == len(nums):
                results.append(path[:])
                return
            for num in nums_dict:
                if nums_dict[num] > 0:
                    path.append(num)
                    nums_dict[num] -= 1
                    backtrack(path, nums_dict)
                    path.pop()
                    nums_dict[num] += 1
        backtrack([], nums_dict)
        return results
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,2]')
    print('Exception :')
    print('[[1,1,2],⁠[1,2,1],⁠[2,1,1]]')
    print('Output :')
    print(str(Solution().permuteUnique([1, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]')
    print('Output :')
    print(str(Solution().permuteUnique([1, 2, 3])))
    print()

    pass
# @lc main=end
