import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # create a minHeap to store the end time of the meeting
        # if the new meeting start time less than the earlies meeting end time
        # we can use the same room, otherwise we need a new room
        endtime_pq = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        rooms = 1
        # push the first end time
        heapq.heappush(endtime_pq, intervals[0][1])
        # now circle through the rest of schedule and check for the meeting end time
        for i in range(1, len(intervals)):
            new_starttime, new_endtime = intervals[i]
            if new_starttime < endtime_pq[0]:
                rooms += 1
                heapq.heappush(endtime_pq, new_endtime)
            else:
                heapq.heappop(endtime_pq)
                heapq.heappush(endtime_pq, new_endtime)
        return rooms
