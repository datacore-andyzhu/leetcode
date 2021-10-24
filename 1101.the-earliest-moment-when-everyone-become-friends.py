from typing import *
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


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # the thinking is like this:
        # we use union find data structure to union nodes together,
        # when number of set is down to 1, we have everyone connected
        # since everyone would have the saeme root?
        uf = UnionFind(n)
        # Do not forget to sort the logs first , otherwise
        # we might run into problem when number of set equal to 1
        # and we output wrong timestamp
        logs.sort(key=lambda x: x[0])
        for time, node0, node1 in logs:
            uf.union(node0, node1)
            if uf.size == 1:
                return time

        return -1
