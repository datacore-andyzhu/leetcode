# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Option 1: use the Resursive method"""
        # result = []
        # def traverse(root):
        #     if not root:
        #         return []
        #     traverse(root.left)
        #     traverse(root.right)
        #     result.append(root.val)

        # traverse(root)

        # return result

        """Option 2: use the iterative method #1"""
        # if not root:
        #     return []
        # result = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)

        # return result[::-1]

        """Option 3: use the Iterative method #2"""
        if not root:
            return []
        result = []
        stack = []
        last_visited = None
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != last_visited:
                    node = peek.right
                else:
                    last_visited = stack.pop()
                    result.append(last_visited.val)
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,3]')
    print('Exception :')
    print('[3,2,1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1, None, 2, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1, 2]))))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1, None, 2]))))
    print()

    pass
# @lc main=end
