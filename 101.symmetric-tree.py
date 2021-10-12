# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#


# @lc tags=tree;depth-first-search;breadth-first-search

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(node1, node2):
            if node1 and not node2:
                return False
            elif node2 and not node1:
                return False
            elif not node1 and not node2:
                return True
            elif node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    return sym(node1.left, node2.right) and sym(node1.right, node2.left)

        if root is None:
            return False

        return sym(root.left, root.right)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,2,3,4,4,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSymmetric(listToTreeNode([1, 2, 2, 3, 4, 4, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,2,null,3,null,3]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSymmetric(
        listToTreeNode([1, 2, 2, None, 3, None, 3]))))
    print()

    pass
# @lc main=end
