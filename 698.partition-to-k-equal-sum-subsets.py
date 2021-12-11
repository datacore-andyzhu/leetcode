# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#


# @lc tags=dynamic-programming;recursion

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
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k > n:
            return False
        if sum(nums) % k != 0:
            return False
        bucket = [0 for _ in range(k)]
        target = sum(nums) // k
        used = [False for _ in range(n)] # if nums[i] is used or not
        def backtrack(nums, k, bukcet_sum, used, start, target):
            # if all k buckets filled up
            if k == 0:
                return True
            # current bucket filled up, go for the next bucket
            if bukcet_sum == target:
                return backtrack(nums, k-1, 0, used, 0, target)
            
            for i in range(start, n):
                # if the number is already used
                if used[i]:
                    continue
                # if sum is overflow the backet can hold
                if nums[i] + bukcet_sum > target:
                    continue
                used[i] = True
                bukcet_sum += nums[i]
                if backtrack(nums, k, bukcet_sum, used, i+1, target):
                    return True
                bukcet_sum -= nums[i]
                used[i] = False
            return False
        return backtrack(nums, k, 0, used, 0, target)

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,3,2,3,5,2,1], k = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canPartitionKSubsets([4,3,2,3,5,2,1],4)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4], k = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canPartitionKSubsets([1,2,3,4],3)))
    print()
    
    pass
# @lc main=end