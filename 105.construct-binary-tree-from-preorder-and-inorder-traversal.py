# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, preStart, preEnd, inorder, inStart, inEnd):
            if preStart > preEnd:
                return None
            rootVal = preorder[preStart]
            inorder_root_idx = 0
            for i in range(len(inorder)):
                if inorder[i] == rootVal:
                    inorder_root_idx = i
                    break
            root = TreeNode(rootVal)
            leftSize = inorder_root_idx - inStart
            root.left = build(preorder, preStart+1, preStart +
                              leftSize, inorder, inStart, inorder_root_idx-1)
            root.right = build(preorder, preStart+leftSize+1,
                               preEnd, inorder, inorder_root_idx+1, inEnd)

            return root
        return build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        """ Solution 2 """
        def buildFromInorder(left, right):
            if left > right:
                return None
            rootVal = preorder.popleft()
            root = TreeNode(rootVal)
            inorder_idx = inorder_map[rootVal]
            # due to preorder sequence of put the node
            # we need to start from root.left
            root.left = buildFromInorder(left, inorder_idx-1)
            root.right = buildFromInorder(inorder_idx+1, right)
            return root
        preorder = deque(preorder)
        inorder_map = {value: index for index, value in enumerate(inorder)}
        return buildFromInorder(0, len(preorder)-1)
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]')
    print('Exception :')
    print('[3,9,20,null,null,15,7]')
    print('Output :')
    print(str(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('preorder = [-1], inorder = [-1]')
    print('Exception :')
    print('[-1]')
    print('Output :')
    print(str(Solution().buildTree([-1], [-1])))
    print()

    pass
# @lc main=end
