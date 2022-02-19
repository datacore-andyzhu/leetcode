# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """ Solution 1: Use O(n) with heap """
#         if not root:
#             return None
#         stack = []
#         pq = []
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             heapq.heappush(pq, (abs(target-root.val), root.val))
#             root = root.right
#         ans = []
#         for i in range(k):
#             ans.append(heapq.heappop(pq)[1])

#         return ans

        """ Solution 2: """
        ans = []
        lowerStack = []
        upperStack = []
        p = root
        while p:
            if p.val < target:
                lowerStack.append(p)
                p = p.right
            else:
                upperStack.append(p)
                p = p.left

        def getUpperNext(node, stack):
            p = node
            while p:
                stack.append(p)
                p = p.left

        def getLowerNext(node, stack):
            p = node
            while p:
                stack.append(p)
                p = p.right

        for i in range(k):
            if len(lowerStack) == 0:
                top = upperStack.pop()
                ans.append(top.val)
                getUpperNext(top.right, upperStack)
            elif len(upperStack) == 0:
                top = lowerStack.pop()
                ans.append(top.val)
                getLowerNext(top.left, lowerStack)
            elif upperStack[-1].val - target <= target - lowerStack[-1].val:
                top = upperStack.pop()
                ans.append(top.val)
                getUpperNext(top.right, upperStack)
            elif len(upperStack) == 0 or target - lowerStack[-1].val < upperStack[-1].val - target:
                top = lowerStack.pop()
                ans.append(top.val)
                getLowerNext(top.left, lowerStack)
        return ans
