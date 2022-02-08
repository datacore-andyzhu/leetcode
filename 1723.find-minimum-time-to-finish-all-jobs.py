# @lc app=leetcode id=1723 lang=python3
#
# [1723] Find Minimum Time to Finish All Jobs
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
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(limit):
            arr = sorted(jobs)

            groups = [0] * k
            # 分成K 组，看看在这个limit 下 能不能安排完工作
            if dfs(arr, groups, limit):
                return True
            else:
                return False

        def dfs(arr, groups, limit):
            # 尝试每种可能性
            #print(arr, groups, limit)
            if not arr:  # 分完，则方案可行
                return True
            v = arr.pop()

            for i in range(k):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if dfs(arr, groups, limit):
                        return True
                    groups[i] -= v
                # 如果这个工人分活失败（给他分配这个任务后所有的尝试都是失败的），则剪枝，因为也没必要再往后试了，其他人也会出现一样的情况
                if groups[i] == 0:
                    break
            arr.append(v)
            return False

        #每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        left, right = max(jobs), sum(jobs)

        while left < right:
            mid = (left + right)//2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('jobs = [3,2,3], k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minimumTimeRequired([3,2,3],3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('jobs = [1,2,4,7,8], k = 2')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().minimumTimeRequired([1,2,4,7,8],2)))
    print()
    
    pass
# @lc main=end
