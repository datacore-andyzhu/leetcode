class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i = j = 0
        while i < len(slots1) and j < len(slots2):
            overlap_start = max(slots1[i][0], slots2[j][0])
            overlap_end = min(slots1[i][1], slots2[j][1])
            if overlap_end - overlap_start >= duration:
                return [overlap_start, overlap_start + duration]
            else:
                if slots1[i][1] < slots2[j][1]:
                    i += 1
                else:
                    j += 1
        return []
