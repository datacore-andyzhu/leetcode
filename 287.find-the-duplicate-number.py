# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
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
    def findDuplicate(self, nums: List[int]) -> int:
        """ Solution 1 O(nlogn)"""
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        # return -1

        """ Solution 2 O(n) """
        # slow = nums[0]
        # fast = nums[0]
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         fast = nums[0]
        #         while fast != slow:
        #             slow = nums[slow]
        #             fast = nums[fast]
        #         return slow

        """ Solution 3 """
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1
        #     if nums[index] > 0:
        #         nums[index] *= -1
        #     else:
        #         return index +1

        """ SOlution 4 """
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)
        # return -1

        """ Solution 5 """
        low = 1
        high = len(nums) - 1
        while low <= high:
            mid = low + (high-low)//2
            count = 0
            for a in nums:
                if a <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid - 1
        return low

        """ Solution 6 """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    return nums[i]
                swap(nums, i, nums[i]-1)

        return -1
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,4,2,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findDuplicate([1,3,4,2,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,1,3,4,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findDuplicate([3,1,3,4,2])))
    print()
    
    pass
# @lc main=end
