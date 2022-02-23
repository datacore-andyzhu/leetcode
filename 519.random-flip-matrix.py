# @lc app=leetcode id=519 lang=python3
#
# [519] Random Flip Matrix
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
""" Solution 1 """


class ReservoirSampling:
    def __init__(self, n):
        self.n = n
        self.build()

    def build(self):
        self.m = {}
        self.l = self.n

    def get_next(self):
        self.l = self.l - 1
        r = random.randint(0, self.l)
        v = self.m.get(r, r)
        self.m[r] = self.m.get(self.l, self.l)
        return v

    def reset(self):
        self.build()


class Solution:
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.rs = ReservoirSampling(n_rows * n_cols)

    def flip(self):
        """
        :rtype: List[int]
        """
        n = self.rs.get_next()
        return self.n2rc(n)

    def n2rc(self, n):
        r = n // self.n_cols
        c = n - r * self.n_cols
        return [r, c]

    def reset(self):
        """
        :rtype: void
        """
        self.rs.reset()


""" Solution 2 """
# class Solution:

#     def __init__(self, m: int, n: int):
#         self.c = n
#         self.end = m * n - 1
#         self.d = {}
#         self.start = 0
#     def flip(self) -> List[int]:
#         rand = random.randint(self.start, self.end)
#         res = self.d.get(rand, rand)
#         self.d[rand] = self.d.get(self.start, self.start)
#         self.start += 1
#         return divmod(res, self.c)


#     def reset(self) -> None:
#         self.d = {}
#         self.start = 0
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error,error)))
    print()
    
    pass
# @lc main=end
