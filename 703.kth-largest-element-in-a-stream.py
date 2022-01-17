# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#


# @lc tags=Unknown

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
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.heapSize = k
        heapq.heapify(self.minHeap)
        if self.heapSize < len(nums):
            for i in range(self.heapSize):
                heapq.heappush(self.minHeap, nums[i])
            for j in range(self.heapSize, len(nums)):
                if nums[j] > self.minHeap[0]:
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap, nums[j])
        else:
            for i in range(len(nums)):
                heapq.heappush(self.minHeap, nums[i])


    def add(self, val: int) -> int:
        if self.heapSize == len(self.minHeap):
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error,error)))
    print()
    
    pass
# @lc main=end
