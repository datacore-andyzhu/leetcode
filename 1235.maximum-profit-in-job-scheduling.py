# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
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
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def findNextJob(startTime, lastEndTime):
            start = 0
            end = len(startTime) - 1
            nextIndex = len(startTime)
            while start <= end:
                mid = start + (end - start) // 2
                if startTime[mid] >= lastEndTime:
                    nextIndex = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return nextIndex

        def findMaxProfit(jobs, startTime):
            length = len(startTime)
            for position in range(length-1, -1, -1):
                curr_profit = 0
                nextIndex = findNextJob(startTime, jobs[position][1])
                if nextIndex != length:
                    curr_profit = jobs[position][2] + memo[nextIndex]
                else:
                    curr_profit = jobs[position][2]
                if position == length - 1:
                    memo[position] = curr_profit
                else:
                    memo[position] = max(curr_profit, memo[position+1])
            return memo[0]
        memo = [0] * 50001
        job_length = len(startTime)
        jobs = []
        for i in range(job_length):
            job_tuple = (startTime[i], endTime[i], profit[i])
            jobs.append(job_tuple)

        jobs.sort(key=lambda x: x[0])

        for i in range(job_length):
            startTime[i] = jobs[i][0]
        return findMaxProfit(jobs, startTime)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]')
    print('Exception :')
    print('120')
    print('Output :')
    print(str(Solution().jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit =[20,20,100,70,60]')
    print('Exception :')
    print('150')
    print('Output :')
    print(str(Solution().jobScheduling([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().jobScheduling([1,1,1],[2,3,4],[5,6,4])))
    print()
    
    pass
# @lc main=end
