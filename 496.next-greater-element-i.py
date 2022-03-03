# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
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
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ SOlution 1 """
#         num_dict = defaultdict(int)
#         m = len(nums1) - 1
#         n = len(nums2)
#         for i in range(n-1):
#             for j in range (i+1, n):
#                 if nums2[i] < nums2[j]:
#                     num_dict[nums2[i]] = nums2[j]
#                     break
#             else:
#                 num_dict[nums2[i]] = -1
#         num_dict[nums2[-1]] = -1

#         res = []
#         for num in nums1:
#             res.append(num_dict[num])

#         return res
        """ Solution 2 """
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [4,1,2], nums2 = [1,3,4,2]')
    print('Exception :')
    print('[-1,3,-1]')
    print('Output :')
    print(str(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [2,4], nums2 = [1,2,3,4]')
    print('Exception :')
    print('[3,-1]')
    print('Output :')
    print(str(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4])))
    print()

    pass
# @lc main=end
