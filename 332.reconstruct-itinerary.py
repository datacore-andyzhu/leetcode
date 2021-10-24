# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#


# @lc tags=depth-first-search;graph

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
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        def buildGraph(tickets):
            _graph = {}
            for src, dst in tickets:
                if src not in _graph:
                    _graph[src] = [dst]
                else:
                    _graph[src].append(dst)
                if dst not in _graph:
                    _graph[dst] = []
            for arr in _graph.values():
                arr.sort(reverse=True)
            return _graph
        # Hierholzer's Algo (Eulerian Path): visit every edge exactly once (allow for revisit vertices)

        def dfs(origin, graph):
            destList = graph[origin]
            while destList:
                nextDest = destList.pop()
                dfs(nextDest, graph)
            itinerary.append(origin)
        graph = buildGraph(tickets)
        itinerary = []
        dfs('JFK', graph)

        return itinerary[::-1]

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]')
    print('Exception :')
    print('["JFK","MUC","LHR","SFO","SJC"]')
    print('Output :')
    print(str(Solution().findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]')
    print('Exception :')
    print('["JFK","ATL","JFK","SFO","ATL","SFO"]')
    print('Output :')
    print(str(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], [
          "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])))
    print()

    pass
# @lc main=end
