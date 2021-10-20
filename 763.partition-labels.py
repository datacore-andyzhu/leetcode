# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#


# @lc tags=string;recursion

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
    def partitionLabels(self, s: str) -> List[int]:
        """ Solution 1"""
        # if len(s) == 1:
        #     return [1]
        # pos_dict = {}
        # # scan through all the string and record each char start position
        # # and end position
        # for i in range(len(s)):
        #     if s[i] not in pos_dict:
        #         # cannot use the tuple here becasue tuple is not allowed for assignment later
        #         pos_dict[s[i]] = [i, i]
        #     else:
        #         pos_dict[s[i]][1] = i
        # # now use the above dictionary to build interval list
        # intervals = []
        # for value in pos_dict.values():
        #     intervals.append(value)
        # # sort the intervals by start position
        # intervals.sort(key=lambda x: x[0])

        # # merge the intervals
        # result = []
        # start = intervals[0][0]
        # end = intervals[0][1]
        # for _start, _end in intervals[1:]:
        #     if _start < end:
        #         start = min(start, _start)
        #         end = max(end, _end)
        #     else:
        #         result.append((start, end))
        #         start = _start
        #         end = _end
        # result.append((start, end))

        # # now prepare the return value
        # output = []
        # for i in range(len(result)):
        #     output.append(result[i][1]-result[i][0] + 1)
        # return output

        """ Solution 2, not necessary easier to understand"""
        # bit simpler solution
        # create a dictionary to save all tehe char's right most position
        # then go through the string again, if char's index matches its right most pisition, 
        # 'cut' the string
        charMaxPos = {}
        for i in range(len(s)):
            charMaxPos[s[i]] = i
        
        start = 0
        scannedCharMaxPos = 0 # scanned char max position
        result = []
        for i in range(len(s)):
            curCharMaxPos = charMaxPos[s[i]] # get current char mas position
            scannedCharMaxPos = max(scannedCharMaxPos, curCharMaxPos) # need to return most right posiiton of char
            if i == scannedCharMaxPos: # right at the sweet spot, no such char will find any more, 'cut' it
                result.append(i - start + 1)
                start = i + 1
        
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ababcbacadefegdehijhklij"')
    print('Exception :')
    print('[9,7,8]')
    print('Output :')
    print(str(Solution().partitionLabels("ababcbacadefegdehijhklij")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "eccbbbbdec"')
    print('Exception :')
    print('[10]')
    print('Output :')
    print(str(Solution().partitionLabels("eccbbbbdec")))
    print()

    pass
# @lc main=end
