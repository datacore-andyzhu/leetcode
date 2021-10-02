# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
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
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter_dict = {}
        for num in nums:
            if counter_dict.get(num, 0) == 0:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1
            if counter_dict[num] >= 2:
                return True
        return False

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsDuplicate([1,2,3,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().containsDuplicate([1,2,3,4])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1,1,1,3,3,4,3,2,4,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])))
    print()
    
    pass
# @lc main=end