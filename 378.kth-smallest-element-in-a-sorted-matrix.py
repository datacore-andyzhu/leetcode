# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#


# @lc tags=binary-search;heap

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
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """ Solution 1: use Heap """
        # n = len(matrix)
        # heap = [(matrix[i][0], i, 0) for i in range(n)]
        # heapq.heapify(heap)
        # for i in range(k-1):
        #     num, x, y = heapq.heappop(heap)
        #     if y != n-1:
        #         heapq.heappush(heap, (matrix[x][y+1], x, y+1))
        # return heapq.heappop(heap)[0]

        """ Solution 2: binary search """
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8')
    print('Exception :')
    print('13')
    print('Output :')
    print(str(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('matrix = [[-5]], k = 1')
    print('Exception :')
    print('-5')
    print('Output :')
    print(str(Solution().kthSmallest([[-5]],1)))
    print()
    
    pass
# @lc main=end
