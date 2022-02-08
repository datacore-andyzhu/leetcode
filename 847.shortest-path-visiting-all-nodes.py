# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
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
import collections
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        ans = (1 << n) - 1  # 1111
        queue = collections.deque()
        visited = set()
        steps = 0
        for i in range(n):
            queue.append((i, 1 << i))

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node, state = queue.popleft()
                if state == ans:
                    return steps
                if (node, state) in visited:
                    continue
                visited.add((node, state))
                for nxtnode in graph[node]:
                    if (nxtnode, state | (1 << nxtnode)) not in visited:
                        queue.append((nxtnode, state | (1 << nxtnode)))
            steps += 1

        return -1
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2,3],[0],[0],[0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().shortestPathLength([[1,2,3],[0],[0],[0]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])))
    print()
    
    pass
# @lc main=end
