"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if len(schedule) == 0:
            return []
        _schedule = []
        for emp_schedule in schedule:
            for interval in emp_schedule:
                _schedule.append(interval)

        _schedule.sort(key=lambda x: (x.start, x.end))

        res = []
        prev = _schedule[0]

        for curr in _schedule[1:]:
            if curr.start <= prev.end:
                prev.end = max(curr.end, prev.end)
            else:
                # print(prev.end, curr.start)
                _interval = Interval(prev.end, curr.start)
                res.append(_interval)
                prev = curr
        return res
