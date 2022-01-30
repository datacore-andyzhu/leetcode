# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#


# @lc tags=Unknown

# @lc imports=start
from imports import *
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


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        else:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
            return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """ Solution 1: Using Kruskal's Algorithm """
#         edgeLists = []
#         n = len(points)
#         for i in range(n):
#             for j in range(n):
#                 if i != j:
#                     dist = abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])
#                     edgeLists.append((i, j, dist))
#         edgeLists.sort(key=lambda x:x[2])

#         costs = 0
#         uf = UnionFind(n)
#         for edge in edgeLists:
#             if not uf.connected(edge[0], edge[1]):
#                 uf.union(edge[0], edge[1])
#                 costs += edge[2]
#         return costs
        """ Solution 2: Using Prim's Algorithm """
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        visited = [False] * size
        result = 0
        count = size - 1
        # Add all edges from points[0] vertexs
        x1, y1 = points[0]
        for j in range(1, size):
            # Calculate the distance between two coordinates.
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, j, cost)
            pq.append(edge)

        # Convert pq to a heap.
        heapq.heapify(pq)

        visited[0] = True
        while pq and count > 0:
            edge = heapq.heappop(pq)
            point1 = edge.point1
            point2 = edge.point2
            cost = edge.cost
            if not visited[point2]:
                result += cost
                visited[point2] = True
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                            abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq, Edge(point2, j, distance))
                count -= 1
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[0,0],[2,2],[3,10],[5,2],[7,0]]')
    print('Exception :')
    print('20')
    print('Output :')
    print(str(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('points = [[3,12],[-2,5],[-4,1]]')
    print('Exception :')
    print('18')
    print('Output :')
    print(str(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]])))
    print()
    
    pass
# @lc main=end
