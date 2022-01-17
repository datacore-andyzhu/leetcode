import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            nextStick = stick1 + stick2
            cost += nextStick
            heapq.heappush(sticks, nextStick)
        return cost
