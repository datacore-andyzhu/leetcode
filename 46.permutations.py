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
        """ Solution 1 """
        # def backtrack(nums, path):
        #     if len(path) == len(nums):
        #         result.append(path[:])
        #         return

        #     for num in nums:
        #         if num in path:
        #             continue
        #         path.append(num)
        #         backtrack(nums, path)
        #         path.pop()

        # result = []
        # backtrack(nums, [])
        # return result
        """ Solution 2 """
        def backtrack(nums, used, path):
            if len(path) == len(nums):
                results.append(path[:])
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums, used, path)
                path.pop()
                used[i] = False
        results = []
        # use list to indicate which index's number has been used
        used = [False for _ in range(len(nums))]
        backtrack(nums, used, [])
        return results

        """ Solution 3 """
        res = []

        def _dfs(cur, rest):
            if not rest:
                res.append(cur)
            for i in range(len(rest)):
                _dfs(cur+[rest[i]], rest[0:i] + rest[i+1:])

        _dfs([], nums)
        return res

        """ solution 4 """
        queue = [[]]
        level = 0
        while queue:
            # popleft node
            l = len(queue)

            for _ in range(l):
                cur = queue.pop(0)
                for j in range(len(nums)):
                    if nums[j] not in cur:
                        new = cur + [nums[j]]
                        queue.append(new)
            level += 1
            if level == len(nums):
                return queue
        return []


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
