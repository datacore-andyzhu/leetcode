# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ','.join(map(str, postorder(root)))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def traversal(low=float('-inf'), high=float('inf')):
            if not data or data[-1] < low or data[-1] > high:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = traversal(val, high)
            root.left = traversal(low, val)
            return root
        data = [int(x) for x in data.split(',') if x]

        return traversal()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [2,1,3]')
    print('Exception :')
    print('[2,1,3]')
    print('Output :')
    print(str(Solution().serialize(listToTreeNode([2,1,3]))))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().serialize(listToTreeNode([]))))
    print()
    
    pass
# @lc main=end
