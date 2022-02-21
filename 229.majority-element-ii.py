# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#


# @lc tags=array

# @lc imports=start
import collections
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
    def majorityElement(self, nums: List[int]) -> List[int]:
        """ Solution 1: use Moore voting algo """
        ans = []
        ele1, ele2 = 0, 0
        vote1, vote2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == ele1:
                vote1 += 1
            elif vote2 > 0 and num == ele2:
                vote2 += 1
            elif vote1 == 0:
                ele1 = num
                vote1 += 1
            elif vote2 == 0:
                ele2 = num
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == ele1:
                cnt1 += 1
            if vote2 > 0 and num == ele2:
                cnt2 += 1
        if vote1 > 0 and cnt1 > len(nums) // 3:
            ans.append(ele1)
        if vote2 > 0 and cnt2 > len(nums) // 3:
            ans.append(ele2)
        
        return ans

        """ Solution 2: Hash table """
        majority = collections.Counter(nums)

        ans = []
        for key in majority.keys():
            if majority[key] > len(nums) // 3:
                ans.append(key)
        return ans
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,3]')
    print('Exception :')
    print('[3]')
    print('Output :')
    print(str(Solution().majorityElement([3,2,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().majorityElement([1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().majorityElement([1,2])))
    print()
    
    pass
# @lc main=end