# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#


# @lc tags=Unknown

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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        lst1 = dfs(root1)
        lst2 = dfs(root2)
        result = []
        i = 0
        j = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                result.append(lst1[i])
                i += 1
            else:
                result.append(lst2[j])
                j += 1

        while i < len(lst1):
            result.append(lst1[i])
            i += 1
        while j < len(lst2):
            result.append(lst2[j])
            j += 1
        return result

        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root1 = [2,1,4], root2 = [1,0,3]')
    print('Exception :')
    print('[0,1,1,2,3,4]')
    print('Output :')
    print(str(Solution().getAllElements(
        listToTreeNode([2, 1, 4]), listToTreeNode([1, 0, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root1 = [1,null,8], root2 = [8,1]')
    print('Exception :')
    print('[1,1,8,8]')
    print('Output :')
    print(str(Solution().getAllElements(
        listToTreeNode([1, None, 8]), listToTreeNode([8, 1]))))
    print()

    pass
# @lc main=end
