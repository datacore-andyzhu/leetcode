# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
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
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def buildGraph(n, dislikes):
            graph = {}

            for i in range(1, n+1):
                graph[i] = []
            for v, w in dislikes:
                graph[v].append(w)
                graph[w].append(v)
            return graph

        def dfs(graph, node, visited, colors):
            nonlocal result
            if not result:
                return
            # if visited[node]:
            #     return
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    colors[neighbor] = ~colors[node]
                    dfs(graph, neighbor, visited, colors)
                else:
                    if colors[neighbor] == colors[node]:
                        result = False
        visited = [False] * (n + 1)
        colors = [0] * (n + 1)
        result = True
        graph = buildGraph(n, dislikes)
        for i in range(1, n+1):
            if not visited[i]:
                dfs(graph, i, visited, colors)
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4, dislikes = [[1,2],[1,3],[2,4]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3, dislikes = [[1,2],[1,3],[2,3]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().possibleBipartition(3, [[1, 2], [1, 3], [2, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().possibleBipartition(
        5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])))
    print()

    pass
# @lc main=end
