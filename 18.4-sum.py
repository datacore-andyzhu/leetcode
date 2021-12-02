# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


# @lc tags=array;hash-table;two-pointers

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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                p = n - 1
                while k < p:
                    while k > j+1 and k < n and nums[k] == nums[k-1]:
                        k += 1
                    if k >= p:
                        break
                    curr_sum = nums[i] + nums[j] + nums[k] + nums[p]
                    if curr_sum == target:
                        ans.append([nums[i], nums[j], nums[k], nums[p]])
                        k += 1
                        p -= 1
                    elif curr_sum < target:
                        k += 1
                    elif curr_sum > target:
                        p -= 1
        return ans
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,0,-1,0,-2,2], target = 0')
    print('Exception :')
    print('[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]')
    print('Output :')
    print(str(Solution().fourSum([1, 0, -1, 0, -2, 2], 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,2,2,2], target = 8')
    print('Exception :')
    print('[[2,2,2,2]]')
    print('Output :')
    print(str(Solution().fourSum([2, 2, 2, 2, 2], 8)))
    print()

    pass
# @lc main=end
