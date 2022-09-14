Fenwick Tree (Binary Index Tree)

Range Updates and Range Query

```python
class myFenwickTree:
    def __init__(self, nums):
        self.n = len(nums) - 1
        self.diff = [0] * (n+1)
        self.tree = [0] * (n+1)
        self.helpertree = [0] * (n+1)
        
        for i in range(1, n+1):
            self.diff[i] = nums[i] - nums[i-1]
        for i in range(1, n+1):
            self.add(self.tree, i, self.diff[i])
            self.add(self.helpertree, i, (i-1)*diff[i])
    def sum(self, left, right):
        preSum0 = (left -1) * self.query(tree, left-1) - self.query(self.helpertree, left-1)
        preSum1 = right * self.query(tree, right) - self.query(helpertree, right)
       	return preSum1 - preSum0
    
    def rangeUpdate(self,left, right, val):
        self.add(self.tree, left, val)
        self.add(self.tree, right+1, -val)
        self.add(self.helpertree, left, (left-1)*val)
        self.add(self.helpertree, right+1, right*(-val))
    
    def query(self, thisTree, k):
        ans = 0
        for i in range(k, 0, lowbit(i)):
            ans += thisTree[i]
        return ans
    
    def add(self, thisTree, k, val):
        for i in range(k, self.n+1, lowbit(i)):
            thisTree[i] += val
    def lowbit(self, i):
        return i & -i

```

