# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
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
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # since heapq is a min-heap
        # we use negative of the numbers to mimic a max-heap
        evens = []
        minimum = inf
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num*2)
                minimum = min(minimum, num*2)
        heapq.heapify(evens)
        min_deviation = inf
        while evens:
            current_value = -heapq.heappop(evens)
            min_deviation = min(min_deviation, current_value-minimum)
            if current_value % 2 == 0:
                minimum = min(minimum, current_value//2)
                heapq.heappush(evens, -current_value//2)
            else:
                # if the maximum is odd, break and return
                break
        return min_deviation
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minimumDeviation([1,2,3,4])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [4,1,5,20,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minimumDeviation([4,1,5,20,3])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [2,10,8]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minimumDeviation([2,10,8])))
    print()
    
    pass
# @lc main=end
