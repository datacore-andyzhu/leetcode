# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc tags=heap;sliding-window

# @lc imports=start
import collections
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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        windowQueue = collections.deque()
        res = []
        # building a monotone decline queue where front of queue always 
        # has the larghest number 
        # this time instead of store the number
        # we store the index of the number
        # the windowsQueuep[0] == i-k is very important to pop previous 
        # max number
        for i in range(len(nums)):
            if windowQueue and windowQueue[0] == i-k:
                windowQueue.popleft()
            while windowQueue and nums[i] > nums[windowQueue[-1]]:
                windowQueue.pop()
            windowQueue.append(i)

            if i >= k-1:
                res.append(nums[windowQueue[0]])
        return res
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,-1,-3,5,3,6,7], k = 3')
    print('Exception :')
    print('[3,3,5,5,6,7]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1], k = 1')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([1], 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,-1], k = 1')
    print('Exception :')
    print('[1,-1]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([1, -1], 1)))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [9,11], k = 2')
    print('Exception :')
    print('[11]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([9, 11], 2)))
    print()

    print('Example 5:')
    print('Input : ')
    print('nums = [4,-2], k = 2')
    print('Exception :')
    print('[4]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([4, -2], 2)))
    print()

    pass
# @lc main=end
