# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#


# @lc tags=array

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
    def kthGrammar(self, n: int, k: int) -> int:
        """
        观察下面的规律，把每一行对半分开
        1、0
        2、0 | 1
        3、01 | 10
        4、0110 | 1001
        5、01101001 | 10010110
        6、0110100110010110 | 1001011001101001

        发现每一行的前半段就是上一行，后半段就是上一行的每个值反过来（0变1，1变0）

        可以分为两种情况
        如果K在前半段，所对应的值就是上一行的第K个值
        如果K在后半段，可以先算出K相对于后半段的位置，然后找出上一行这个位置的值，把值反过来

        """
        if n == 1:
            return 0

        # // 计算当前行的长度：2的N-1次方
        length = 2**(n-1)
        # 如果K大于长度的一半，就是K所在位置是后半段
        if k > length // 2:
            # 先得到上一行的值，位置是K相对于后半段的位置
            value = self.kthGrammar(n-1, k-length//2)
            # 然后把值反过来
            return 1 if value == 0 else 0
        else:  # 否则前半部分
            # 值就是上一行K位置的值
            return self.kthGrammar(n-1, k)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1, k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().kthGrammar(1,1)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 2, k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().kthGrammar(2,1)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('n = 2, k = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().kthGrammar(2,2)))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('n = 3, k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().kthGrammar(3,1)))
    print()
    
    pass
# @lc main=end
