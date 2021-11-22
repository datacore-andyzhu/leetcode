# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
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
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # the thought process is to
        # calculate the in_degree of the node
        # if the in_degree is zero that means we need to connect
        in_degree = [0] * n
        out_degree = [0] * n
        result = []
        for _from, _to in edges:
            out_degree[_from] += 1
            in_degree[_to] += 1
        for i in range(n):
            if in_degree[i] == 0 and out_degree[i] != 0:
                result.append(i)
        return result
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]')
    print('Exception :')
    print('[0,3]')
    print('Output :')
    print(str(Solution().findSmallestSetOfVertices(6,[[0,1],[0,2],[2,5],[3,4],[4,2]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]')
    print('Exception :')
    print('[0,2,3]')
    print('Output :')
    print(str(Solution().findSmallestSetOfVertices(5,[[0,1],[2,1],[3,1],[1,4],[2,4]])))
    print()
    
    pass
# @lc main=end
