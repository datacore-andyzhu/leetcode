# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(curr):
            nonlocal pre, result, maxCount, count
            if not curr:
                return
            traversal(curr.left)
            if pre is None:
                count = 1
            elif pre.val == curr.val:
                count += 1
            else:
                count = 1
            pre = curr
            if count == maxCount:
                result.append(curr.val)

            if count > maxCount:
                maxCount = count
                result = [curr.val]

            traversal(curr.right)
            return

        pre = None
        result = []
        count = 0
        maxCount = 0
        traversal(root)
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,2]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().findMode(listToTreeNode([1,None,2,2]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().findMode(listToTreeNode([0]))))
    print()
    
    pass
# @lc main=end
