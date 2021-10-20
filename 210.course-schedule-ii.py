# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#


# @lc tags=depth-first-search;breadth-first-search;graph;topological-sort

# @lc imports=start
import collections
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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ Option 1: Use the recursive (DFS) method plus detecting of the cycle """
        # def buildGraph(numCourses, prerequisities):
        #     graph = {}
        #     for i in range(numCourses):
        #         graph[i] = []
            
        #     for item in prerequisites:
        #         _from = item[1]
        #         _to = item[0]
        #         graph[_from].append(_to)
        #     return graph
        
        # def topSortutil(graph, source, visited, stack):
        #     nonlocal hasCycle
        #     if path[source]:
        #         hasCycle = True
        #     if source in visited or hasCycle:
        #         return
        #     visited.add(source)
        #     path[source] = True
        #     for neighbor in graph[source]:
        #         topSortutil(graph, neighbor, visited, stack)
        #     stack.append(source)
        #     path[source] = False
            
        # visited = set()
        # path = [False] * numCourses
        # stack = []
        # graph = buildGraph(numCourses, prerequisites)
        # hasCycle = False
        # for i in range(numCourses):
        #     topSortutil(graph, i, visited, stack)
        # return stack[::-1] if not hasCycle else []

        """ 
        Option 2: Use the in-degree of the node, we start with vertex whose in degree is zero, remove
        this vertex and go through the other vertex and decrease their in degree by 1, next start with vertex whose
        in degree is zero again, repeat until the graph is empty
        if we cannot find such vertex, we already have a cycle!
        """
        if prerequisites == []:
            return [i for i in range(numCourses)]
        result = []
        graph = {}
        for i  in range(numCourses):
            graph[i] = []
        in_degree_array = [0] * numCourses
        for curr, preq in prerequisites:
            graph[preq].append(curr)
            in_degree_array[curr] += 1
        
        queue = collections.deque([idx for idx, degree in enumerate(in_degree_array) if degree ==0 ])
        visited = 0
        result.extend(queue)
        while queue:
            vertex = queue.popleft()
            visited += 1
            for neighbor in graph[vertex]:
                in_degree_array[neighbor] -= 1
                
                if in_degree_array[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(neighbor)
        return result if visited == numCourses else []
                
            

        


        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numCourses = 2, prerequisites = [[1,0]]')
    print('Exception :')
    print('[0,1]')
    print('Output :')
    print(str(Solution().findOrder(2,[[1,0]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]')
    print('Exception :')
    print('[0,2,1,3]')
    print('Output :')
    print(str(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('numCourses = 1, prerequisites = []')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().findOrder(1,[])))
    print()
    
    pass
# @lc main=end
