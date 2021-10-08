# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#


# @lc tags=array

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
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Scan through the list, when reach a number flip its index's 
        # number to a negative number
        # so for teh missing number's index position will
        # be left positive
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        results = []
        for i in range(len(nums)):
            if nums[i] > 0:
                results.append(i+1)
        return results

        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,3,2,7,8,2,3,1]')
    print('Exception :')
    print('[5,6]')
    print('Output :')
    print(str(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,1]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().findDisappearedNumbers([1,1])))
    print()
    
    pass
# @lc main=end