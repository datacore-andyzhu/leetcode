# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
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
import collections
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverseGraph = {}
        for i in range(n):
            reverseGraph[i] = []
        for i in range(n):
            for dst in graph[i]:
                reverseGraph[dst].append(i)
        reverseIndegrees = {}

        for i in range(n):
            reverseIndegrees[i] = len(graph[i])
        queue = collections.deque()
        for key, value in reverseIndegrees.items():
            if value == 0:
                queue.append(key)

        results = []
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            results.append(node)
            visited.add(node)
            for neighbor in reverseGraph[node]:
                reverseIndegrees[neighbor] -= 1
                if reverseIndegrees[neighbor] == 0:
                    queue.append(neighbor)
        return sorted(results)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2],[2,3],[5],[0],[5],[],[]]')
    print('Exception :')
    print('[2,4,5,6]')
    print('Output :')
    print(str(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]')
    print('Exception :')
    print('[4]')
    print('Output :')
    print(str(Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])))
    print()
    
    pass
# @lc main=end
