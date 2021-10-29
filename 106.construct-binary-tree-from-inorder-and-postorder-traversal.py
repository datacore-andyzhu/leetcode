# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#


# @lc tags=array;tree;depth-first-search

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder, inStart, inEnd, postorder, postStart, postEnd):
            if inStart > inEnd:
                return None
            rootVal = postorder[postEnd]
            inorder_root_idx = 0
            for i in range(len(inorder)):
                if inorder[i] == rootVal:
                    inorder_root_idx = i
                    break
            left_size = inorder_root_idx - inStart
            root = TreeNode(rootVal)
            root.left = build(inorder, inStart, inorder_root_idx-1,
                              postorder, postStart, postStart+left_size-1)
            root.right = build(inorder, inorder_root_idx+1,
                               inEnd, postorder, postStart+left_size, postEnd-1)
            return root
        return build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]')
    print('Exception :')
    print('[3,9,20,null,null,15,7]')
    print('Output :')
    print(str(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('inorder = [-1], postorder = [-1]')
    print('Exception :')
    print('[-1]')
    print('Output :')
    print(str(Solution().buildTree([-1], [-1])))
    print()

    pass
# @lc main=end
