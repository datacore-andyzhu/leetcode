# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc tags=array;hash-table

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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        if len(nums) == 2:
            return [0, 1]
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        # print(hash_table)
        for i in range(len(nums)):
            # print(target-nums[i])
            # We cannot forget the 2nd condition
            # for example[1,3,4,2] for num=3, 6-3 = 3 point back to itself
            if hash_table.get(target-nums[i], 0) != 0 and hash_table.get(target-nums[i], 0) != i:
                return [i, hash_table[target-nums[i]]]
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,7,11,15], target = 9')
    print('Exception :')
    print('[0,1]Because nums[0] + nums[1] == 9, we return [0, 1].')
    print('Output :')
    print(str(Solution().twoSum([2,7,11,15],9)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,4], target = 6')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().twoSum([3,2,4],6)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [3,3], target = 6')
    print('Exception :')
    print('[0,1]')
    print('Output :')
    print(str(Solution().twoSum([3,3],6)))
    print()
    
    pass
# @lc main=end
