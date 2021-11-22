# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#


# @lc tags=string;stack

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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        colors = [False] * len(graph)
        result = True
        def dfs(grah, node):
            nonlocal result
            if not result:
                return 
            # if visited[node]:
            #     return
            visited[node] = True
            for _neighbor in graph[node]:
                if not visited[_neighbor]:
                    colors[_neighbor] = ~ colors[node]
                    dfs(graph, _neighbor)
                else:
                    if colors[_neighbor] == colors[node]:
                        result = False
            return True
        for i in range(len(graph)):
            if not visited[i]:
                dfs(graph, i)
        return result



        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2,3],[0,2],[0,1,3],[0,2]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('graph = [[1,3],[0,2],[1,3],[0,2]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]])))
    print()
    
    pass
# @lc main=end