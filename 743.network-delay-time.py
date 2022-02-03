# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#


# @lc tags=tree

# @lc imports=start
from tkinter import W
from imports import *
import collections
import heapq
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
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """ Solution 1: regular Dijsktra """
        # graph = collections.defaultdict(list)
        # for time in times:
        #     graph[time[0]].append((time[1], time[2]))

        # dist = [float('inf')] * (n+1)
        # dist[0] = 0
        # dist[k] = 0
        # pq = []
        # heapq.heappush(pq, (0, k))
        # visited = set()

        # while pq:
        #     _dist, node = heapq.heappop(pq)
        #     if node in visited:
        #         continue
        #     visited.add(node)
        #     for next, cost in graph[node]:
        #         if _dist + cost < dist[next]:
        #             dist[next] = _dist + cost
        #             heapq.heappush(pq, (_dist+cost, next))

        # if max(dist) == float('inf'):
        #     return -1
        # else:
        #     return max(dist)
        """ Solution 2: Dijkstra without init the distance table """
        # graph = collections.defaultdict(list)
        # for src, dst, weight in times:
        #     graph[src].append((dst, weight))
        # pq = []
        # dist = {}
        # heapq.heappush(pq, (0, k))
        # while pq:
        #     weight, node = heapq.heappop(pq)
        #     if node in dist:
        #         continue
        #     dist[node] = weight
        #     for next, cost in graph[node]:
        #         if next not in dist:
        #             heapq.heappush(pq, (cost+weight, next))
        # return max(dist.values()) if len(dist) == n else -1
        """ Solution 3: Floyd Marchsall """
        # adjMatrix = [[0 for _ in range(n+1) ] for _ in range(n+1)]
        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         adjMatrix[i][j] = adjMatrix[j][i] = float('inf') if i != j else 0
        # for src, dst, weight in times:
        #     adjMatrix[src][dst] = weight
        # # floyd algo, 3 level of loop, DP
        # for p in range(1, n+1):
        #     for i in range(1, n+1):
        #         for j in range(1, n+1):
        #             adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][p]+adjMatrix[p][j])
        # ans = 0
        # for i in range(1, n+1):
        #     ans = max(ans, adjMatrix[k][i])
        
        # return ans if ans < float('inf') else -1

        """ Solution 4: Bellman Ford """
        distance = {i: float('inf') for i in range(1, n+1)}        
        distance[k] = 0

        for i in range(n):
            for u, v, w in times:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
        mx = max(distance.values())
        return mx if mx < float('inf') else -1 

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().networkDelayTime(
        [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('times = [[1,2,1]], n = 2, k = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().networkDelayTime([[1, 2, 1]], 2, 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('times = [[1,2,1]], n = 2, k = 2')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().networkDelayTime([[1, 2, 1]], 2, 2)))
    print()

    pass
# @lc main=end
