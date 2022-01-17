# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#


# @lc tags=two-pointers;sliding-window

# @lc imports=start
from imports import *
import heapq
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
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            remains = abs(stone1) - abs(stone2)
            if remains != 0:
                heapq.heappush(maxHeap, -remains)
        if len(maxHeap) == 1:
            return -maxHeap[0]
        else:
            return 0
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('stones = [2,7,4,1,8,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lastStoneWeight([2,7,4,1,8,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('stones = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lastStoneWeight([1])))
    print()
    
    pass
# @lc main=end
