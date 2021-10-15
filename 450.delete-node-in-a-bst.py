# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
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
    def getMin(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """ Option 1: use recursive method #1 """
        # if root is None:
        #     return None
        # if root.val == key:
        #     # situation 1: the node has no child
        #     if not root.left and not root.right:
        #         return None
        #     # siutaiton 2: only has one child
        #     elif not root.left and root.right:
        #         return root.right
        #     elif root.left and not root.right:
        #         return root.left
        #     # situation 3: has both children
        #     # return smallest number in the right child
        #     elif root.left and root.right:
        #         minNode = self.getMin(root.right)
        #         root.val = minNode.val
        #         # we need to delete the node with min value, not the original key
        #         root.right = self.deleteNode(root.right, minNode.val)
        # elif root.val < key:
        #     root.right = self.deleteNode(root.right, key)
        # else:
        #     root.left = self.deleteNode(root.left, key)
        # return root

        """ Option 2: use resursive method without calling a help function """
        # https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/miao-dong-jiu-wan-shi-liao-by-terry2020-tc0o/
        # if root is None:
        #     return None
        # if root.val == key:
        #     # situation 1: the node has no child
        #     if not root.left and not root.right:
        #         return None
        #     # siutaiton 2: only has one child
        #     elif not root.left and root.right:
        #         return root.right
        #     elif root.left and not root.right:
        #         return root.left
        #     # situation 3: has both children

        #     elif root.left and root.right:
        #         # fina the smallest number in right child
        #         tempNode = root.right
        #         while tempNode.left:
        #             tempNode = tempNode.left
        #         # assign the left child of root to this tempnode
        #         # 将欲删除节点的左子树成为其右子树的最左节点的左子树
        #         tempNode.left = root.left
        #         # 欲删除节点的右子顶替其位置，节点被删除
        #         #
        #         root = root.right

        # elif root.val < key:
        #     root.right = self.deleteNode(root.right, key)
        # else:
        #     root.left = self.deleteNode(root.left, key)
        # return root

        """ Option 3: use iterative method """

        if root is None:
            return None
        curr = root
        prev = None
        while curr is not None and curr.val != key:
            prev = curr
            if curr.val < key:
                curr = curr.right
            else:
                curr = curr.left
        # If we do not find the key
        if curr is None:
            return root

        # if we find the key
        # if key has left or right chold
        # Check if the node to be
        # deleted has atmost one child
        if curr.left == None or\
                curr.right == None:

            # newCurr will replace
            # the node to be deleted.
            newCurr = None

            # if the left child does not exist.
            if curr.left == None:
                newCurr = curr.right
            else:
                newCurr = curr.left

            # check if the node to
            # be deleted is the root.
            if prev == None:
                return newCurr

            # Check if the node to be
            # deleted is prev's left or
            # right child and then
            # replace this with newCurr
            if curr == prev.left:
                prev.left = newCurr
            else:
                prev.right = newCurr

            curr = None

        # node to be deleted
        # has two children.
        else:
            p = None
            temp = None

            # Compute the inorder
            # successor of curr.
            temp = curr.right
            while(temp.left != None):
                p = temp
                temp = temp.left

            # check if the parent of the
            # inorder successor is the root or not.
            # if it isn't, then make the left
            # child of its parent equal to the
            # inorder successor's right child.
            if p != None:
                p.left = temp.right

            else:

                # if the inorder successor was
                # the root, then make the right child
                # of the node to be deleted equal
                # to the right child of the inorder
                # successor.
                curr.right = temp.right

            curr.val = temp.val
            temp = None

        return root


# @lc code=end
# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], key = 3')
    print('Exception :')
    print('[5,4,6,2,null,null,7]')
    print('Output :')
    print(str(Solution().deleteNode(
        listToTreeNode([5, 3, 6, 2, 4, None, 7]), 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], key = 0')
    print('Exception :')
    print('[5,3,6,2,4,null,7]')
    print('Output :')
    print(str(Solution().deleteNode(
        listToTreeNode([5, 3, 6, 2, 4, None, 7]), 0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [], key = 0')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().deleteNode(listToTreeNode([]), 0)))
    print()

    pass
# @lc main=end
