# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#


# @lc tags=hash-table;stack;tree

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Option 1: Use Recursive method"""
        # result = []

        # def traverse(root):
        #     if root is None:
        #         return
        #     traverse(root.left)
        #     result.append(root.val)
        #     traverse(root.right)

        # traverse(root)

        # return result

        """Option 2, Use iterative method"""
        if root is None:
            return []
        result = []
        stack = []
        node = root
        while node or stack:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,3]')
    print('Exception :')
    print('[1,3,2]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1, None, 2, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1, 2]))))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1, None, 2]))))
    print()

    pass
# @lc main=end
