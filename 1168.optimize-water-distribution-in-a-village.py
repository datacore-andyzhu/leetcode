from typing import *
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]
        self.size = n

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # house already connected
        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        self.size -= 1
        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        # we want o build up a list of tuple (cost, house1, house2)
        # for pipes it is easy
        # fbut for well, there is no connect two houses
        # so we imagine a virtual node 0 as the dummy house that each house build well to
        # simulate Kruskal's Algo with Union FInd

        # The overall idea of Kruskal's algorithm is that we iterate through all the edges               # ordered by their costs. For each edge, we decide whether to add it to the final MST.           # The decision is based on whether this new addition will help to connect more dots             # (i.e. vertices).

        # A more concise ***criteria\*** to determine whether we should add a new edge in
        # Kruskal's algorithm is that whether both ends of the edge belong to the
        # same component (group).
        ordered_edge = []
        dummyNode = 0
        for i in range(len(wells)):
            ordered_edge.append((wells[i], dummyNode, i+1))
        for pipe in pipes:
            ordered_edge.append((pipe[2], pipe[0], pipe[1]))
        # order the node by the cost of well or pipe
        ordered_edge.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        total_cost = 0
        for cost, house1, house2 in ordered_edge:
            if uf.union(house1, house2):
                total_cost += cost
        return total_cost
