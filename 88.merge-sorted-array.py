# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc tags=array;two-pointers

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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        while n > 0:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3')
    print('Exception :')
    print('[1,2,2,3,5,6]')
    print('Output :')
    print(str(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums1 = [1], m = 1, nums2 = [], n = 0')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().merge([1],1,[],0)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums1 = [0], m = 0, nums2 = [1], n = 1')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().merge([0],0,[1],1)))
    print()
    
    pass
# @lc main=end
