# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#


# @lc tags=hash-table;two-pointers;binary-search;sort

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
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if len(nums1) > len(nums2):
        #     self.intersect(nums2, nums1)
        # lookup = {}
        # result = []
        # for num in nums1:
        #     lookup[num] = lookup.get(num, 0) + 1

        # for num in nums2:
        #     if lookup.get(num, 0) > 0:
        #         result.append(num)
        #         lookup[num] -= 1
        # return result
        nums1.sort()
        nums2.sort()
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2,2,1], nums2 = [2,2]')
    print('Exception :')
    print('[2,2]')
    print('Output :')
    print(str(Solution().intersect([1, 2, 2, 1], [2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [4,9,5], nums2 = [9,4,9,8,4]')
    print('Exception :')
    print('[4,9]')
    print('Output :')
    print(str(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])))
    print()

    pass
# @lc main=end
