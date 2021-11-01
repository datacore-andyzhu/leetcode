# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#


# @lc tags=divide-and-conquer;heap

# @lc imports=start
from imports import *
from heapq import *
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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in range(k):
            heappush(minheap, nums[i])
        for j in range(k, len(nums)):
            if nums[j] > minheap[0]:
                heappop(minheap)
                heappush(minheap, nums[j])
        return minheap[0]

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,1,5,6,4], k = 2')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,3,1,2,4,5,5,6], k = 4')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)))
    print()

    pass
# @lc main=end
