# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
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
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        The following method is too slow for Python
        So we have to figure out a different way

        """
        # if len(nums) == 1 and nums[0] > k:
        #     return 0
        # if len(nums) == 0:
        #     return 0
        # # first build the preSum arrary, calculate the sum
        # # if we added all the number till certain index (all the way till end)
        # preSum = [0] * (len(nums) + 1)
        # for i in range(1, len(preSum)):
        #     preSum[i] = preSum[i-1] + nums[i-1]
        # count = 0
        # # now go through the preSum array in two loop, and any diiference between
        # # inner and outer equal to k is the asnwer
        # for left in range(len(nums)):
        #     # inner loop start from the already picked outer number
        #     for right in range(left, len(nums)):
        #         if preSum[right+1] - preSum[left] == k:
        #             count += 1
        """
        We have to use a dictionary method, much like the 
        Two Sum problem we solved before
        But this time around, we use the dictionary to store 
        The continuous sum of the original array
        And use cumulative sum minus target to see how many continuous
        array sum is equal to k
        """
        sumDict = {}
        count = 0
        sumDict[0] = 1  # without any number
        sumArr = 0
        for i in range(len(nums)):
            sumArr += nums[i]
            if sumArr - k in sumDict:
                count += sumDict[sumArr-k]
            if sumDict.get(sumArr, 0) == 0:
                sumDict[sumArr] = 1
            else:
                sumDict[sumArr] += 1

        return count
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,1], k = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().subarraySum([1, 1, 1], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3], k = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().subarraySum([1, 2, 3], 3)))
    print()

    pass
# @lc main=end
