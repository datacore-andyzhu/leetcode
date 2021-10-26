from typing import *


class Solution:
    # we use 'NONE' as initial state of WHITE
    GREY = 1
    BLACK = 2
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def buildGraph(n, edges):
            _graph = {i:[] for i in range(n)}

            for edge in edges:
                _graph[edge[0]].append(edge[1])
            return _graph
        
        def dfs(graph, src, dst, states_array):
            if states_array[src] != None:
                return states_array[src] == Solution.BLACK
            
            if len(graph[src]) == 0:
                return src == dst
            
            states_array[src] = Solution.GREY

            for neighbor in graph[src]:
                if not dfs(graph, neighbor, dst, states_array):
                    return False
            states_array[src] = Solution.BLACK

            return True
        graph = {}
        graph = buildGraph(n, edges)
        states_array = [None] * n
        return dfs(graph, source, destination, states_array)

        """ Solution 2 no 3-color coloring """
        # g = defaultdict(set)
        # for e in edges:
        #     g[e[0]].add(e[1])
        # q = [s]
        # u = set([s])
        # while q:
        #     n = q.pop()
        #     if n == d:
        #         if n in g[n] or g[n]:
        #             return False
        #         continue
        #     if not g[n] or n in g[n]:
        #         return False
        #     for nn in g[n]:
        #         if nn in u:
        #             continue
        #         if n in g[nn]:
        #             return False
        #         u.add(nn)
        #         q.append(nn)
        # return True

        """ Solution 3: different way of DFS with visited set (can detect cycle) """
        # if len(edges) == 0:
        #     return source == destination

        # graph = {}
        # visited = {}

        # for s, d in edges:
        #     visited[(s, d)] = False
        #     if s in graph:
        #         graph[s].append(d)
        #     else:
        #         graph[s] = [d]

        #     if d not in graph:
        #         graph[d] = []

        #     if s == destination and s == d:
        #         return False

        # def dfs(node):
        #     if len(graph[node]) == 0:
        #         return node == destination

        #     for neighbor in graph[node]:

        #         if visited[(node, neighbor)]:
        #             return False

        #         visited[(node, neighbor)] = True

        #         ret = dfs(neighbor)

        #         visited[(node, neighbor)] = False
        #         if not ret:
        #             return False

        #     return True

        # return dfs(source)
