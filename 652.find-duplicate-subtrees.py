# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo = defaultdict(int)
        res = []
        def traverse(root):
            if not root:
                return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            subTree = left + "," + right + "," + str(root.val)
            freq = memo.get(subTree, 0)
            if freq == 1:
                res.append(root)
            memo[subTree] += 1
            return subTree
        traverse(root)
        return res
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,null,2,4,null,null,4]')
    print('Exception :')
    print('[[2,4],[4]]')
    print('Output :')
    print(str(Solution().findDuplicateSubtrees(listToTreeNode([1,2,3,4,None,2,4,None,None,4]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [2,1,1]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().findDuplicateSubtrees(listToTreeNode([2,1,1]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [2,2,2,3,null,3,null]')
    print('Exception :')
    print('[[2,3],[3]]')
    print('Output :')
    print(str(Solution().findDuplicateSubtrees(listToTreeNode([2,2,2,3,None,3,None]))))
    print()
    
    pass
# @lc main=end