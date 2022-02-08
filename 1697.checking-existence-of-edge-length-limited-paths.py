# @lc app=leetcode id=1697 lang=python3
#
# [1697] Checking Existence of Edge Length Limited Paths
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


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

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
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        总体思路：一看是无向图，又是确认两个点是否连接，很自然想到并查集。
        但是，题目又加了edge点与点的长度，必须小于query中的查询值的限制。
        所以在这个限制下，如果要检查两个点是否联通前，不能把比query长度大的edge加入并查集中，因为这样会影响点与点是否联通的判断。
        也就是把小于query长度的edge点都连接起来，再使用query中的点参数，在并查集中检查点与点是否联通即可。

        逻辑如下：
        1、对edgeList按照长度正排序；
        2、使用优先队列对queries正排序，并在queries中加一列[3]，原始的位置;
        3、遍历edgeList中的元素edge时：如果edge的长度小于query的长度，结束队列判断；
        4、遍历edgeList中的元素edge时：如果edge的长度大于等于query的长度，
        那么首先队列中的query要出队列，并使用query中的点与点参数，使用并查集来检查联通性，并在返回对象中记录联通性结果；
        其次队列中的query，只要是长度小于等于edge的长度的元素，都要出队列，并做同样的处理；
        5、队列判断处理完后，被遍历的edge元素加入并查集；
        6、最后别忘记，可能队列中可能会有没有处理完的query元素（比如query的查询长度比较大），最后对残留的query，
            要再做一次联通性检查，并记录检查结果；


        """
        edgeList.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        new_queries = [(queries[i], i) for i in range(len(queries))]
        new_queries.sort(key=lambda x: x[0][2])
        ans = [False] * (len(new_queries))
        k = 0
        for query in new_queries:
            while k < len(edgeList) and edgeList[k][2] < query[0][2]:
                uf.union(edgeList[k][0], edgeList[k][1])
                k += 1
            if uf.connected(query[0][0], query[0][1]):
                ans[query[1]] = True
        return ans
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries =[[0,1,2],[0,2,5]]')
    print('Exception :')
    print('[false,true]')
    print('Output :')
    print(str(Solution().distanceLimitedPathsExist(3,[[0,1,2],[1,2,4],[2,0,8],[1,0,16]],[[0,1,2],[0,2,5]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries =[[0,4,14],[1,4,13]]')
    print('Exception :')
    print('[true,false]Exaplanation: The above figure shows the given graph.')
    print('Output :')
    print(str(Solution().distanceLimitedPathsExist(5,[[0,1,10],[1,2,5],[2,3,9],[3,4,13]],[[0,4,14],[1,4,13]])))
    print()
    
    pass
# @lc main=end
