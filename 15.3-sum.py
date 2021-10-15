# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort the array
        # then use two pointers
        result = []
        nums.sort()
        if len(nums) == 0:
            return result
        if nums[0] > 0:
            return result
        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1
            # trick to speed up

            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                tempSum = nums[i] + nums[left] + nums[right]
                if tempSum > 0:
                    right -= 1
                elif tempSum < 0:
                    left += 1
                else:
                    # # Option 1 to avoid duplicate
                    # if [nums[i], nums[left], nums[right]] not in result:
                    #     result.append([nums[i], nums[left], nums[right]])
                    # left += 1
                    # right -= 1
                    
                    # option 2 to avoid duplicate

                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # move to next if duplicates from left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # # move to next if duplicates from right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,0,1,2,-1,-4]')
    print('Exception :')
    print('[[-1,-1,2],[-1,0,1]]')
    print('Output :')
    print(str(Solution().threeSum([-1, 0, 1, 2, -1, -4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().threeSum([])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().threeSum([0])))
    print()

    pass
# @lc main=end
