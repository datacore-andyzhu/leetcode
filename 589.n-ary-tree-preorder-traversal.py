# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            # nonlocal result
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                if child:
                    dfs(child)

        if not root:
            return None
        result = []
        dfs(root)

        return result

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,3,2,4,null,5,6]')
    print('Exception :')
    print('[1,3,5,6,2,4]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root =[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]')
    print('Exception :')
    print('[1,2,3,6,7,11,14,4,8,12,5,9,13,10]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    pass
# @lc main=end
