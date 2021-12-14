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
        """" Solution 1 """
        # graph = {}

        # def buildGraph(tickets):
        #     _graph = {}
        #     for src, dst in tickets:
        #         if src not in _graph:
        #             _graph[src] = [dst]
        #         else:
        #             _graph[src].append(dst)
        #         if dst not in _graph:
        #             _graph[dst] = []
        #     for arr in _graph.values():
        #         arr.sort(reverse=True)
        #     return _graph
        # # Hierholzer's Algo (Eulerian Path): visit every edge exactly once (allow for revisit vertices)

        # def dfs(origin, graph):
        #     destList = graph[origin]
        #     while destList:
        #         nextDest = destList.pop()
        #         dfs(nextDest, graph)
        #     itinerary.append(origin)
        # graph = buildGraph(tickets)
        # itinerary = []
        # dfs('JFK', graph)

        # return itinerary[::-1]

        """ Solution 2: backtrack """
        tickets_graph = defaultdict(list)
        for ticket in tickets:
            tickets_graph[ticket[0]].append(ticket[1])
        
        '''
        tickets_dict里面的内容是这样的
         {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path = ['JFK']
        def backtrack(start_point):
            # base case
            if len(path) == len(tickets) + 1:
                return True
            tickets_graph[start_point].sort()
            for _ in tickets_graph[start_point]:
                # need to remove the point from the list
                # to avoid endlist loop
                end_point = tickets_graph[start_point].pop(0)
                path.append(end_point)
                if backtrack(end_point):
                    return True
                path.pop()
                # put it back
                end_point = tickets_graph[start_point].append(end_point)
        backtrack('JFK')
        return path


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
