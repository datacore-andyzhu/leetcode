# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#


# @lc tags=Unknown

# @lc imports=start
from imports import *
import heapq
import collections
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# 并查集模板


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """ Solution 1: Dijsktra Algo """
        # m = len(heights)
        # n = len(heights[0])
        # distances = [0] + [float('inf')] * (m*n-1)
        # pq = [(0, 0, 0)]
        # visited = set()

        # while pq:
        #     cost, x, y = heapq.heappop(pq)
        #     identity = x*n + y
        #     if identity in visited:
        #         continue
        #     if (x, y) == (m-1, n-1):
        #         break
        #     visited.add(identity)

        #     for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        #         if 0 <= nx < m and 0 <= ny < n and max(cost, abs(heights[x][y] - heights[nx][ny])) <= distances[nx*n+ny]:
        #             distances[nx*n+ny] = max(cost,
        #                                      abs(heights[x][y] - heights[nx][ny]))
        #             heapq.heappush(pq, (distances[nx*n+ny], nx, ny))
        # return distances[m*n-1]
        """ Solution 2: Binary Search """
        # m, n = len(heights), len(heights[0])
        # left, right, ans = 0, 10**6 - 1, 0

        # while left <= right:
        #     mid = (left + right) // 2
        #     q = collections.deque([(0, 0)])
        #     seen = {(0, 0)}

        #     while q:
        #         x, y = q.popleft()
        #         for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        #             if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and abs(heights[x][y] - heights[nx][ny]) <= mid:
        #                 q.append((nx, ny))
        #                 seen.add((nx, ny))

        #     if (m - 1, n - 1) in seen:
        #         ans = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1

        # return ans
        """ Solution 3: Union Find """
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append(
                        (iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append(
                        (iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.unite(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break

        return ans

@lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('heights = [[1,2,2],[3,8,2],[5,3,5]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('heights = [[1,2,3],[3,8,4],[5,3,5]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('heights =[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])))
    print()
    
    pass
# @lc main=end
