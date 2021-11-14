# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#


# @lc tags=depth-first-search;breadth-first-search;graph

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

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}
    """ Solution 1: DFS """
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])

        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(i) for i in node.neighbors]

        return clone_node
    """ Slution 2: BFS approach """
    def cloneGraphBFS(self, node: 'Node') -> 'Node':
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.


        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        self.visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in self.visited:
                    # Clone the neighbor and put in the visited, if not present already
                    self.visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                self.visited[n].neighbors.append(self.visited[neighbor])

        # Return the clone of the node from visited.
        return self.visited[node]

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('adjList = [[2,4],[1,3],[2,4],[1,3]]')
    print('Exception :')
    print('[[2,4],[1,3],[2,4],[1,3]]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('adjList = [[]]')
    print('Exception :')
    print('[[]]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 3:')
    print('Input : ')
    print('adjList = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 4:')
    print('Input : ')
    print('adjList = [[2],[1]]')
    print('Exception :')
    print('[[2],[1]]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    pass
# @lc main=end
