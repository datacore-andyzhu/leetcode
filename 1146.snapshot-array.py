# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#


# @lc tags=string

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


class SnapshotArray:

    def __init__(self, length: int):

        # use dict of dict, first layer for the index and second leyer for snapshot id
        self.snapshots = {}
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        if index in self.snapshots:
            self.snapshots[index][self.snapId] = val
        else:
            self.snapshots[index] = {self.snapId: val}

    def snap(self) -> int:
        res = self.snapId
        self.snapId += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snapshots:
            if snap_id in self.snapshots[index]:
                return self.snapshots[index][snap_id]

            closest_snapId = -1
            # here the snapid actual return the key of the dict
            for snapid in self.snapshots[index]:
                if snapid < snap_id:
                    closest_snapId = max(snapid, closest_snapId)
            if closest_snapId != -1:
                return self.snapshots[index][closest_snapId]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
        pass
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('["SnapshotArray","set","snap","set","get"][[3],[0,5],[],[0,6],[0,0]]')
    print('Exception :')
    print('[null,null,0,null,5]')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end
