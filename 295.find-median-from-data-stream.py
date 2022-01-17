# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#


# @lc tags=heap;design

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
class MedianFinder:

    def __init__(self):
        # 2nd half of the data stream
        self.minHeap = []        
        # 1st half of the data stream
        self.maxHeap = []       
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.minHeap, num)
            heapq.heappush(self.maxHeap, -1 * (heapq.heappop(self.minHeap)))
        else:
            heapq.heappush(self.maxHeap, - num)
            heapq.heappush(self.minHeap, - heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (self.minHeap[0] + (-1*self.maxHeap[0])) / 2
        else:
            return float(-1 * self.maxHeap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
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
    print(str(Solution().__init__()))
    print()
    
    pass
# @lc main=end
