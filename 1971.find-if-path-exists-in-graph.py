# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#


# @lc tags=Unknown

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


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.size = n

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.size -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        """ Solution 1: use explicit stack to solve """
        # graph = {}

        # def buildGraph(edges):
        #     _graph = defaultdict(list)
        #     for edge in edges:
        #         if edge[0] in _graph:
        #             _graph[edge[0]].append(edge[1])
        #         else:
        #             _graph[edge[0]] = [edge[1]]
        #         if edge[1] in _graph:
        #             _graph[edge[1]].append(edge[0])
        #         else:
        #             _graph[edge[1]] = [edge[0]]
        #     return _graph
        # graph = buildGraph(edges)
        # traverse_stack = [start]
        # visited = set()
        # while traverse_stack:
        #     vertex = traverse_stack.pop()
        #     if vertex not in visited:
        #         visited.add(vertex)
        #         if vertex == end:
        #             return True
        #         for neighbor in graph[vertex]:
        #             traverse_stack.append(neighbor)
        # return False
        """ Solution 2: DFS with recursive function """
        # def dfs(graph, node, visited):
        #     if node == end:
        #         return True
        #     visited[node] = True
        #     for neighbor in graph[node]:
        #         if not visited[neighbor]:
        #             if dfs(graph, neighbor, visited):
        #                 return True

        #     return False
        # # we can use special way to convert edge list into graph adjacent list
        # # because of the special case in this problem (node is from 0 to n-1)
        # graph = {i:[] for i in range(n)}
        # for edge in edges:
        #     graph[edge[0]] += [edge[1]]
        #     graph[edge[1]] += [edge[0]]
        # visited = [False for _ in range(n)]
        # return dfs(graph, start, visited)

        """ Solution 3: Use Union Find data structure and test if start anmd end is connected"""
        # uf = UnionFind(n)
        # for edge in edges:
        #     uf.union(edge[0], edge[1])

        # return uf.connected(start, end)

        """ Solution 4: Use BFS to determine if there is an path exists from start to end """
        graph = {}

        def buildGraph(n, edges):
            _graph = {i: [] for i in range(n)}
            for edge in edges:
                _graph[edge[0]].append(edge[1])
                _graph[edge[1]].append(edge[0])
            return _graph

        graph = buildGraph(n, edges)
        traverse_queue = collections.deque([start])
        visited = set()
        while traverse_queue:
            vertex = traverse_queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                if vertex == end:
                    return True
                for neighbor in graph[vertex]:
                    traverse_queue.append(neighbor)
        return False


# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validPath(
        6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)))
    print()

    pass
# @lc main=end
