# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        For Binary search tree, while traversing the tree from top to bottom the first node which lies in 
        between the two numbers n1 and n2 is the LCA of the nodes, i.e. the first node n with the lowest 
        depth which lies in between n1 and n2 (n1<=n<=n2) n1 < n2. So just recursively traverse the BST in, 
        if node’s value is greater than both n1 and n2 then our LCA lies in the left side of the node, 
        if it’s is smaller than both n1 and n2, then LCA lies on the right side. Otherwise, 
        the root is LCA (assuming that both n1 and n2 are present in BST).
        """
        """
        For Binary search tree, while traversing the tree from top to bottom the first node which lies in between the 
        two numbers n1 and n2 is the LCA of the nodes, i.e. the first node n with the lowest depth which lies in between 
        n1 and n2 (n1<=n<=n2) n1 < n2. So just recursively traverse the BST in, if node’s value is greater than both n1 and n2 
        then our LCA lies in the left side of the node, if it’s is smaller than both n1 and n2, then LCA lies on the right side. 
        Otherwise, the root is LCA (assuming that both n1 and n2 are present in BST).
        """
        if root is None:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5],2,8)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5],2,4)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [2,1], p = 2, q = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().lowestCommonAncestor([2,1],2,1)))
    print()
    
    pass
# @lc main=end
