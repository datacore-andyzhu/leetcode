
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first, last = None, None

        def traverse(node):
            if not node:
                return None
            nonlocal last, first
            traverse(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node

            traverse(node.right)

        if not root:
            return None
        traverse(root)
        last.right = first
        first.left = last
        return first
