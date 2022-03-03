# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#


# @lc tags=string;backtracking;greedy

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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, lst):
            if not root:
                return None
            if not root.left and not root.right:
                lst.append(root.val)
                return
            dfs(root.left, lst)
            dfs(root.right, lst)
        lst1 = []
        lst2 = []
        dfs(root1, lst1)
        dfs(root2, lst2)
        if len(lst1) != len(lst2):
            return False
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
        return True
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().leafSimilar(listToTreeNode([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), listToTreeNode(
        [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root1 = [1,2,3], root2 = [1,3,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().leafSimilar(listToTreeNode(
        [1, 2, 3]), listToTreeNode([1, 3, 2]))))
    print()

    pass
# @lc main=end
