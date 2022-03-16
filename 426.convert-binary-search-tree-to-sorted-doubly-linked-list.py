
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """ Solution 1 """
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

        """ SOlution 2 """
        if not root:
            return None
        first, last = None, None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not first:
                first = root
            if last:
                last.right = root
                root.left = last
            last = root
            root = root.right
        last.right = first
        first.left = last
        return first
