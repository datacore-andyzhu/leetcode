# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc tags=binary-search;dynamic-programming

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
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ Solution 1 """
        # n = len(nums)
        # sub = [nums[0]]

        # for num in nums[1:]:
        #     if num > sub[-1]:
        #         sub.append(num)
        #     else:
        #         # find the first element in sub that is grater than or
        #         # equal to num
        #         i = 0
        #         while num > sub[i]:
        #             i += 1
        #         sub[i] = num

        # return len(sub)
        """ Solution 2 use bianry search instead of linear scan to replace num in sub """
        """
        Initialize an array sub which contains the first element of nums.

        Iterate through the input, starting from the second element. For each element num:

        If num is greater than any element in sub, then add num to sub.
        
        Otherwise, perform a binary search in sub to find the smallest element 
        that is greater than or equal to num. Replace that element with num.
        Return the length of sub.
        """
        # sub = []
        # for num in nums:
        #     i = bisect_left(sub, num)

        #     # If num is greater than any element in sub
        #     if i == len(sub):
        #         sub.append(num)

        #     # Otherwise, replace the first element in sub greater than or equal to num
        #     else:
        #         sub[i] = num

        # return len(sub)
        """ Solution 3: DP """
        n = len(nums)
        if n <= 1:
            return n
        # dp[i] represent up to i the longest increase sub sequence
        dp = [1 for _ in range(n)]
        result = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] > result:
                result = dp[i]
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [10,9,2,5,3,7,101,18]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1,0,3,2,3]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [7,7,7,7,7,7,7]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7])))
    print()

    pass
# @lc main=end
