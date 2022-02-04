# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#


# @lc tags=tree;depth-first-search

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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        graph = defaultdict(list)

        def buildGraph(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                buildGraph(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                buildGraph(root.right)
        buildGraph(root)
        # for key, value in graph.items():
        #     print(key, value)
        queue = collections.deque()
        queue.append(target.val)
        visited = set()
        result = []
        while queue and k >= 0:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if k == 0:
                    result.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            k -= 1
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2')
    print('Exception :')
    print('[7,4,1]')
    print('Output :')
    print(str(Solution().distanceK(listToTreeNode([3,5,1,6,2,0,8,None,None,7,4]),listToTreeNode(5),2)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1], target = 1, k = 3')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().distanceK(listToTreeNode([1]),listToTreeNode(1),3)))
    print()
    
    pass
# @lc main=end
