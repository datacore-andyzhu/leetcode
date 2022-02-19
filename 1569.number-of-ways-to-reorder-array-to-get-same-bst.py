# @lc app=leetcode id=1569 lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
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


class TNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.size = 1
        self.ans = 0


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def insert(val: int):
            cur = root
            while True:
                cur.size += 1
                if val < cur.value:
                    if not cur.left:
                        cur.left = TNode(val)
                        return
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = TNode(val)
                        return
                    cur = cur.right

        def dfs(node: TNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            lsize = node.left.size if node.left else 0
            rsize = node.right.size if node.right else 0
            lans = node.left.ans if node.left else 1
            rans = node.right.ans if node.right else 1
            node.ans = c[lsize + rsize][lsize] * lans * rans % mod

        n = len(nums)
        if n == 1:
            return 0

        mod = 10**9 + 7
        c = [[0] * n for _ in range(n)]
        c[0][0] = 1
        for i in range(1, n):
            c[i][0] = 1
            for j in range(1, n):
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod

        root = TNode(nums[0])
        for i in range(1, n):
            val = nums[i]
            insert(val)

        dfs(root)
        return (root.ans - 1 + mod) % mod


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,1,3]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numOfWays([2,1,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,4,5,1,2]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().numOfWays([3,4,5,1,2])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numOfWays([1,2,3])))
    print()
    
    pass
# @lc main=end
