class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """ Solution 1 """
        # def dfs(lower=float('-inf'), upper=float('inf')):
        #     nonlocal idx, length
        #     if idx == length:
        #         return True
        #     if preorder[idx] < lower or preorder[idx] > upper:
        #         return False
        #     curr = preorder[idx]
        #     idx += 1
        #     if dfs(lower, curr):
        #         return True
        #     if dfs(curr, upper):
        #         return True
        #     return False
        # idx = 0
        # length = len(preorder)
        # if length == 0:
        #     return True
        # return dfs()

        """ Soltuion 2: use stack and minVal"""
        ## https://www.youtube.com/watch?v=Psce8aMuX8s
        # the preorder should have a sequence of large --> small(est) --> large, like a trough, both end are large
        if not preorder or len(preorder) == 0:
            return False
        minVal = float('-inf')
        stack = []
        for num in preorder:
            if num < minVal:
                return False
            while stack and stack[-1] < num:
                minVal = stack.pop()
            stack.append(num)
        return True
