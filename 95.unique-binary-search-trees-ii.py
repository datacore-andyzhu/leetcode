# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#


# @lc tags=dynamic-programming;tree

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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end+1):
                # all possible left subtree if i chosen as root
                left_trees = generateTrees(start, i-1)
                # all possible right subtree if i chosen as root
                right_trees = generateTrees(i+1, end)

                # connect left and right subtree with i as root
                for l in left_trees:
                    for r in right_trees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        all_trees.append(curr_tree)
            return all_trees

        return generateTrees(1, n) if n else []
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]')
    print('Output :')
    print(str(Solution().generateTrees(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().generateTrees(1)))
    print()

    pass
# @lc main=end
