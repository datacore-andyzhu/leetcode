# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc tags=hash-table;heap

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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleDict = defaultdict(int)
        for num in nums:
            eleDict[num] -= 1
        minheap = []
        # the python heapq seems sorted on the 1st element of the tuple
        # that's why we put in tuple like (value, key)
        for key, value in eleDict.items():
            heappush(minheap, (value, key))
        result = []
        for i in range(k):
            result.append(heappop(minheap)[1])
        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,1,2,2,3], k = 2')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1], k = 1')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().topKFrequent([1], 1)))
    print()

    pass
# @lc main=end
