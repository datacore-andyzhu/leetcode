# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#


# @lc tags=depth-first-search;breadth-first-search;graph;topological-sort

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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ Method 1"""
        # hasCycle = False
        # visited = set()
        # path = [False for _ in range(numCourses)]

        # def buildGraph(numCourses, prerequisites):
        #     graph = defaultdict(list)
        #     for i in range(numCourses):
        #         graph[i] = []

        #     for relation in prerequisites:
        #         _from = relation[1]
        #         _to = relation[0]
        #         graph[_from].append(_to)
        #     return graph

        # def traverse(graph, vertex, visited, path):
        #     nonlocal hasCycle
        #     if path[vertex]:
        #         hasCycle = True
        #     if vertex in visited or hasCycle:
        #         return
        #     visited.add(vertex)
        #     path[vertex] = True
        #     for neighbor in graph[vertex]:
        #         traverse(graph, neighbor, visited, path)
        #     path[vertex] = False

        # graph = buildGraph(numCourses, prerequisites)
        # for i in range(numCourses):
        #     traverse(graph, i, visited, path)
        # return not hasCycle

        """ Method 2"""
        visited = set()
        path = [False for _ in range(numCourses)]

        def buildGraph(numCourses, prerequisites):
            graph = defaultdict(list)
            for i in range(numCourses):
                graph[i] = []

            for relation in prerequisites:
                _from = relation[1]
                _to = relation[0]
                graph[_from].append(_to)
            return graph

        def hasCycle(graph, vertex, visited, path):
            
            if path[vertex]:
                return True
            if vertex in visited:
                return False
            visited.add(vertex)
            path[vertex] = True
            for neighbor in graph[vertex]:
                if hasCycle(graph, neighbor, visited, path):
                    return True
            path[vertex] = False
            return False

        graph = buildGraph(numCourses, prerequisites)
        for i in range(numCourses):
            if hasCycle(graph, i, visited, path):
                return False
        return True
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numCourses = 2, prerequisites = [[1,0]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canFinish(2, [[1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('numCourses = 2, prerequisites = [[1,0],[0,1]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canFinish(2, [[1, 0], [0, 1]])))
    print()

    pass
# @lc main=end
