class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        if not order or len(order) == 0:
            return 0
        import sortedcontainers
        """
        Use a TreeMap to store each value’s depth. Initially, value order[0] has depth 1.

        Loop over the remaining elements in order. 
        For each value curr, find the two adjacent values of curr in the TreeMap, 
        which are prev and next such that prev <= curr <= next. 
        If both values exist (not null), then since both prev and next come before curr, 
        the depth of curr is the maximum of the depths of prev and next plus 1. 
        If only one value exists, then the depth of curr is the depth of the existing value plus 1.
        """
        maxDepth = 1
        sd = sortedcontainers.SortedDict()
        for x in order:
            k = sd.bisect_left(x)
            val = 1
            if k:
                val = 1 + sd.values()[k-1]
            if k < len(sd):
                val = max(val, 1 + sd.values()[k])
            sd[x] = val
            maxDepth = max(maxDepth, val)
        return maxDepth  # max(sd.values())
