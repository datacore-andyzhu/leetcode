# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#


# @lc tags=tree;design

# @lc imports=start
import collections
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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        bfs = collections.deque([root])
        arr = []
        while bfs:
            node = bfs.popleft()
            if node is None:
                arr.append('null')
            else:
                arr.append(str(node.val))
                bfs.append(node.left)
                bfs.append(node.right)
        while arr[-1] is None:
            arr.pop()
        return ','.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split(',')
        node_arr = [TreeNode(arr[i]) for i in range(len(arr))]
       
        print(arr)
        # since we prebuild the array with Treenode
        # there is no need for set root, etc again
        # since the leaf node is half of the tree, we only need
        # to iterate through half of the tree
        n = len(arr)//2
        
        for i in range(n):
            
  
            node_arr[i].left = node_arr[i*2+1]
            node_arr[i].right = node_arr[i*2+2]
  
        return node_arr[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,null,null,4,5]')
    print('Exception :')
    print('[1,2,3,null,null,4,5]')
    print('Output :')
    print(str(Solution().serialize([1, 2, 3, null, null, 4, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().serialize([])))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().serialize([1])))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().serialize([1, 2])))
    print()

    pass
# @lc main=end
