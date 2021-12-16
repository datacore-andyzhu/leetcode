# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#


# @lc tags=breadth-first-search;graph

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
    """
    Initially, we would build a graph with the adjacency list from the input.

    We then create a queue which would be used to hold the leaf nodes.

    At the beginning, we put all the current leaf nodes into the queue.

    We then run a loop until there is only two nodes left in the graph.

    At each iteration, we remove the current leaf nodes from the queue. While removing the nodes, we also remove the edges that are linked to the nodes. As a consequence, some of the non-leaf nodes would become leaf nodes. And these are the nodes that would be trimmed out in the next iteration.

    The iteration terminates when there are no more than two nodes left in the graph, which are the desired centroids nodes.
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4, edges = [[1,0],[1,2],[1,3]]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().findMinHeightTrees(4,[[1,0],[1,2],[1,3]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]')
    print('Exception :')
    print('[3,4]')
    print('Output :')
    print(str(Solution().findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('n = 1, edges = []')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().findMinHeightTrees(1,[])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('n = 2, edges = [[0,1]]')
    print('Exception :')
    print('[0,1]')
    print('Output :')
    print(str(Solution().findMinHeightTrees(2,[[0,1]])))
    print()
    
    pass
# @lc main=end
