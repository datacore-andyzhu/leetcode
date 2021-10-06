# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#


# @lc tags=hash-table;math

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
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes
        prime = [True] * (n + 1)

        if n < 2:
            return 0
        count = 0
        i = 2
        while i**2 <= n:
            if prime[i] == True:

                for j in range(i**2, n+1, i):
                    prime[j] = False
            i += 1
        for i in range(2, n):
            if prime[i] == True:
                count += 1
        return count

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().countPrimes(10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countPrimes(0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countPrimes(1)))
    print()

    pass
# @lc main=end
