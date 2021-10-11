# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#


# @lc tags=stack;tree

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Option 1: Use recursive method"""
        # result = []

        # def traverse(root):
        #     if root is None:
        #         return []
        #     result.append(root.val)
        #     traverse(root.left)
        #     traverse(root.right)

        # traverse(root)

        # return result

        """Option 2: Use the Iterative method"""
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,3]')
    print('Exception :')
    print('[1,2,3]')
    print('Output :')
    print(str(Solution().preorderTraversal(listToTreeNode([1, None, 2, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().preorderTraversal(listToTreeNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().preorderTraversal(listToTreeNode([1]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().preorderTraversal(listToTreeNode([1, 2]))))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().preorderTraversal(listToTreeNode([1, None, 2]))))
    print()

    pass
# @lc main=end
