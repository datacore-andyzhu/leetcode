# @lc app=leetcode id=1786 lang=python3
#
# [1786] Number of Restricted Paths From First to Last Node
#


# @lc tags=Unknown

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
import heapq
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7
        distance = [0]+ [float('inf')] * (n)
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        for src, dst, weight in edges:
            graph[src].append((dst, weight))
            graph[dst].append((src, weight))
        
        distance[n] = 0
        pq = []
        heapq.heappush(pq, (0, n))
        visited = set()
        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            for dst, weight in graph[node]:
                if dst not in visited:
                    new_cost = cost + weight
                    if new_cost < distance[dst]:
                        distance[dst] = new_cost
                        heapq.heappush(pq, (new_cost, dst))
        # now it comes down to the DP part
        dp = defaultdict(int)
        dp[n] = 1
        distance_dict = {}
        for idx, value in enumerate(distance):
            if idx == 0: continue
            distance_dict[idx] = value
        print(distance_dict)
        node_list = [ x[0] for x in sorted(list(distance_dict.items()), key=lambda x: x[1])]
        for u in node_list:
            for v, _ in graph[u]:
                if distance_dict[v] > distance_dict[u]:
                    dp[v] += dp[u]
            if u == 1:
                break
        return dp[1] % mod
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5, edges =[[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().countRestrictedPaths(5,[[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 7, edges =[[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().countRestrictedPaths(7,[[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]])))
    print()
    
    pass
# @lc main=end