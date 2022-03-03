# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#


# @lc tags=stack;tree;design

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


class BSTIterator:
    """ Solution 1 """
    def __init__(self, root: Optional[TreeNode]):
        self.btree = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.btree.append(root.val)
            inorder(root.right)
        self.idx = -1
        inorder(root)

    def next(self) -> int:
        self.idx += 1
        return self.btree[self.idx]

    def hasNext(self) -> bool:
        if self.idx + 1 < len(self.btree):
            return True
        return False

    """ Solution 2 """

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end
