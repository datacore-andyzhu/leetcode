# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc tags=array;divide-and-conquer;bit-manipulation

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
    def majorityElement(self, nums: List[int]) -> int:
        # use Boyer-Moore Voting algorithm
        # other algorithm here:
        # https://www.enjoyalgorithms.com/blog/find-the-majority-element-in-an-array
        """
        Here is an interesting analogy to understand the algorithm: suppose we have n number of people, each holding one element of the array. Then, whenever two people find each other where neither holds the same array element as the other, they sit down. Eventually, in the end, if anyone is left standing, then that element is the majority element. Since the majority element occurs more than n/2 times, you can guarantee that this approach will always find the majority element.

        Solution Steps

        To keep track of our current guess of the majority element, we declare the variable majorityCandidate and maintain a variable counter. Initially, the value of both variables is equal to 0.
        Let’s walk across the array, if the current element matches our guess, we increment the counter by1. If the current element doesn’t match our guess, then we decrement the counter by 1. (Think!)
        If the value of the counter is equal to 0, then we reset the current guess and make it equal to the current element. i.e majorityCandidate = X[i]. In other words, we forget about everything up to the previous index and consider the current element as the potential candidate for the majority element in the array. 
        By the end of the loop, the value of the majority element gets stored in the variable majorityCandidate.
        """
        majority_candidate = 0
        counter = 0
        for i in range(len(nums)):
            if counter == 0:
                majority_candidate = nums[i]
            if majority_candidate == nums[i]:
                counter += 1
            else:
                counter -= 1
        return majority_candidate

        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().majorityElement([3,2,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,1,1,1,2,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().majorityElement([2,2,1,1,1,2,2])))
    print()
    
    pass
# @lc main=end
