# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def backtrack(root, path):
            # because we have to use pre-order traversal
            # so we need to append the root.val
            path.append(str(root.val))
            # we reach the leaf node
            if not root.left and not root.right:
                result.append('->'.join(path))
                return
            if root.left:
                # since we append the root.val in line 39, we don't
                # need to append root.left.val at all
                backtrack(root.left, path)
                path.pop()
            if root.right:
                # since we append the root.val in line 39, we don't
                # need to append root.left.val at all
                backtrack(root.right, path)
                path.pop()

        if not root:
            return []
        backtrack(root, [])
        return result

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,null,5]')
    print('Exception :')
    print('["1->2->5","1->3"]')
    print('Output :')
    print(str(Solution().binaryTreePaths(listToTreeNode([1, 2, 3, None, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('["1"]')
    print('Output :')
    print(str(Solution().binaryTreePaths(listToTreeNode([1]))))
    print()

    pass
# @lc main=end
