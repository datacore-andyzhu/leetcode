# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#


# @lc tags=math;heap

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
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        numbers = [1]
	# initial heap, (the next val to be evaluated, the idx of the prime number, the last time used number position
        h = [(p, idx, 0) for idx, p in enumerate(primes)]
        heapq.heapify(h)
        while len(numbers) < n:
	    # check the smallest number
            v, idx_p, num_pos = heapq.heappop(h)
	# if can put in the result
            if len(numbers) == 0 or v > numbers[-1]:
                numbers.append(v)
		# put the next candidate by putting the primes * the next can use number in the dp list
            heapq.heappush(
                h, (primes[idx_p] * numbers[num_pos+1], idx_p, num_pos+1))
        return numbers[-1]
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 12, primes = [2,7,13,19]')
    print('Exception :')
    print('32')
    print('Output :')
    print(str(Solution().nthSuperUglyNumber(12,[2,7,13,19])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1, primes = [2,3,5]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().nthSuperUglyNumber(1,[2,3,5])))
    print()
    
    pass
# @lc main=end
