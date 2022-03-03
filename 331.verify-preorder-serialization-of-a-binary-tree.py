# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#


# @lc tags=stack

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


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """ Solution 1: Stack """
        # https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/
        # preorder_list = preorder.split(',')
        # stack = []
        # for i in range(len(preorder_list)):
        #     stack.append(preorder_list[i])
        #     while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
        #         stack.pop()
        #         stack.pop()
        #         stack.pop()
        #         stack.append('#')
        # return len(stack) == 1 and stack[-1] == '#'

        """ Solutuion 2: count in and out degree of tree: """
        # any non leaf node, except the root, has 1 in and 2 out
        # root node has 2 out
        # any leaf node only has 1 in
        # for a valid tree:
        # in < out until the very last and when tree traversed all the ndoes ins == outs
        # and number of non empty nodes with child  m >=n (n is number of empty nodes)
        preorder_list = preorder.split(',')
        ins = 0
        outs = 0
        for i in range(len(preorder_list)):
            if preorder_list[i] != '#':
                outs += 2
            if i != 0:
                ins += 1
            if i != len(preorder_list)-1 and outs <= ins:
                return False
        print(ins, outs)
        return ins == outs
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")))
    print()

    print('Example 2:')
    print('Input : ')
    print('preorder = "1,#"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValidSerialization("1,#")))
    print()

    print('Example 3:')
    print('Input : ')
    print('preorder = "9,#,#,1"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValidSerialization("9,#,#,1")))
    print()

    pass
# @lc main=end
