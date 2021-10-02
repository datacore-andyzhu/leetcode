# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#


# @lc tags=array;two-pointers;binary-search

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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]
        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numbers = [2,7,11,15], target = 9')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().twoSum([2,7,11,15],9)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('numbers = [2,3,4], target = 6')
    print('Exception :')
    print('[1,3]')
    print('Output :')
    print(str(Solution().twoSum([2,3,4],6)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('numbers = [-1,0], target = -1')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().twoSum([-1,0],-1)))
    print()
    
    pass
# @lc main=end