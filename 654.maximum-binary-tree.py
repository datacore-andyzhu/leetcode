# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums, low, high):
            if low > high or low < 0 or high > len(nums):
                return None

            index = -1
            max_value = -1
            for i in range(low, high+1):
                if max_value < nums[i]:
                    max_value = nums[i]
                    index = i

            root = TreeNode(max_value)
            root.left = build(nums, low, index-1)
            root.right = build(nums, index+1, high)

            return root
        return build(nums, 0, len(nums)-1)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,1,6,0,5]')
    print('Exception :')
    print('[6,3,5,null,2,0,null,null,1]')
    print('Output :')
    print(str(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,1]')
    print('Exception :')
    print('[3,null,2,null,1]')
    print('Output :')
    print(str(Solution().constructMaximumBinaryTree([3, 2, 1])))
    print()

    pass
# @lc main=end
