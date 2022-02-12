"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
import collections

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = collections.defaultdict(Node)
        while p:
            if not p.parent:
                parents[p] = p.parent
            else:
                parents[p] = p
            p = p.parent

        while q:
            if q in parents:
                return q
            elif q.parent in parents:

                return q.parent
            else:
                q = q.parent
        return None
