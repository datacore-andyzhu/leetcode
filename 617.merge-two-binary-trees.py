# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#


# @lc tags=tree

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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """  Solution 1: Recursive method """
#         if root1 is None:
#             return root2
#         if root2 is None:
#             return root1
#         root1.val = root1.val + root2.val
#         root1.left = self.mergeTrees(root1.left, root2.left)
#         root1.right = self.mergeTrees(root1.right, root2.right)

#         return root1
        """ Solution 2: Iterative method level order traversal """
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        bfs = collections.deque([(root1, root2)])

        while bfs:
            node1, node2 = bfs.popleft()

            if node1 is None or node2 is None:
                continue
            node1.val += node2.val
            if node1.left is None:
                node1.left = node2.left
            else:
                bfs.append((node1.left, node2.left))
            if node1.right is None:
                node1.right = node2.right
            else:
                bfs.append((node1.right, node2.right))

        return root1
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]')
    print('Exception :')
    print('[3,4,5,5,4,null,7]')
    print('Output :')
    print(str(Solution().mergeTrees(listToTreeNode([1,3,2,5]),listToTreeNode([2,1,3,None,4,None,7]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root1 = [1], root2 = [1,2]')
    print('Exception :')
    print('[2,2]')
    print('Output :')
    print(str(Solution().mergeTrees(listToTreeNode([1]),listToTreeNode([1,2]))))
    print()
    
    pass
# @lc main=end
