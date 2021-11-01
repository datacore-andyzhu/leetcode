# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        stack = [root]
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        # While traversing the tree, keep saving the parent pointers.
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node

        # Ancestors set() for node p.
        ancestor = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestor.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestor:
            q = parent[q]
        return q


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().lowestCommonAncestor(
        [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], 5, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().lowestCommonAncestor(
        [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], 5, 4)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,2], p = 1, q = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lowestCommonAncestor([1, 2], 1, 2)))
    print()

    pass
# @lc main=end
