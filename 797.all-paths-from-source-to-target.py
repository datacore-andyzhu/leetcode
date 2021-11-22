# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#


# @lc tags=hash-table;math

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
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, src, dst, visited, path):
            nonlocal results
            if src == dst:
                results.append(path.copy())
            if visited[src]:
                return
            visited[src] = True
            for neighbor in graph[src]:
                path.append(neighbor)
                dfs(graph, neighbor, dst, visited, path)
                path.pop()
            # do not forget to reset the visited hashmap
            # becasue this is finding all the path
            visited[src] = False
        results = []
        n = len(graph)
        visited = [False for _ in range(n)]
        path = [0]
        dfs(graph, 0, n-1, visited, path)
        return results

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2],[3],[3],[]]')
    print('Exception :')
    print('[[0,1,3],[0,2,3]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1, 2], [3], [3], []])))
    print()

    print('Example 2:')
    print('Input : ')
    print('graph = [[4,3,1],[3,2,4],[3],[4],[]]')
    print('Exception :')
    print('[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget(
        [[4, 3, 1], [3, 2, 4], [3], [4], []])))
    print()

    print('Example 3:')
    print('Input : ')
    print('graph = [[1],[]]')
    print('Exception :')
    print('[[0,1]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1], []])))
    print()

    print('Example 4:')
    print('Input : ')
    print('graph = [[1,2,3],[2],[3],[]]')
    print('Exception :')
    print('[[0,1,2,3],[0,2,3],[0,3]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1, 2, 3], [2], [3], []])))
    print()

    print('Example 5:')
    print('Input : ')
    print('graph = [[1,3],[2],[3],[]]')
    print('Exception :')
    print('[[0,1,2,3],[0,3]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1, 3], [2], [3], []])))
    print()

    pass
# @lc main=end
