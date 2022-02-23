# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ Solution 1: recursive"""
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        """ Solution 2: iterative """

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        deq = deque()
        deq.append((p, q))
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('p = [1,2,3], q = [1,2,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSameTree(listToTreeNode([1,2,3]),listToTreeNode([1,2,3]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('p = [1,2], q = [1,null,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSameTree(listToTreeNode([1,2]),listToTreeNode([1,None,2]))))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('p = [1,2,1], q = [1,1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSameTree(listToTreeNode([1,2,1]),listToTreeNode([1,1,2]))))
    print()
    
    pass
# @lc main=end
