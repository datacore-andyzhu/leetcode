> T1 and T2 are two very large binary trees. Create an algorithm to determine if T2 is a subtree of T1.
>
> A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.
>
> Note: This problem is slightly different from the original problem.
>
> Example1:
>
>  Input: t1 = [1, 2, 3], t2 = [2]
>  Output: true
> Example2:
>
>  Input: t1 = [1, null, 2, 4], t2 = [3, 2]
>  Output: false
> Note:
>
> The node numbers of both tree are in [0, 20000].
>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def checksub(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            return checksub(t1.left, t2.left) and checksub(t1.right, t2.right)

        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        
        if t1.val == t2.val:
            return checksub(t1, t2)
        return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
```

