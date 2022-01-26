 Example 1770. Maximum Score from Performing Multiplication Operations

------

> For this problem, we will again start by looking at a top-down approach.

In this article, we're going to be looking at the problem [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/). We can tell this is a DP problem because it is asking for a maximum score, and every time we choose to use a number from \text{nums}nums, it affects all future possibilities. Let's solve this problem with the framework:

\1. A **function or array** that answers the problem for a given state

Since we're doing top-down, we need to decide on two things for our function \text{dp}dp. What state variables we need to pass to it, and what it will return. We are given two input arrays: \text{nums}nums and \text{multipliers}multipliers. The problem says we need to do \text{m}m operations, and on the i^{th}*i**t**h* operation, we gain score equal to \text{multipliers[i]}multipliers[i] times a number from either the left or right end of \text{nums}nums, which we remove after the operation. That means we need to know 3 things for each operation:

1. How many operations have we done so far; this tells us what number from \text{multipliers}multipliers we will be using?
2. The index of the leftmost number remaining in \text{nums}nums.
3. The index of the rightmost number remaining in \text{nums}nums.

We can use one state variable, \text{i}i, to indicate how many operations we have done so far, which means \text{multipliers[i]}multipliers[i] is the current multiplier to be used. For the leftmost number remaining in \text{nums}nums, we can use another state variable, \text{left}left, that indicates how many left operations we have done so far. If we have done, say 3 left operations, if we were to do another left operation we would use \text{nums[3]}nums[3] (because nums is 0-indexed). We can say the same thing for the rightmost remaining number - let's use a state variable \text{right}right that indicates how many right operations we have done so far.

It may seem like we need all 3 of these state variables, but we can formulate an equation for one of them using the other two. If we know how many elements we have picked from the leftside, \text{left}left, and we know how many elements we have picked in total, \text{i}i, then we know that we must have picked \text{i - left}i - left elements from the rightside. The original length of \text{nums}nums is \text{n}n, which means the index of the rightmost element is \text{right = n - 1 - (i - left)}right = n - 1 - (i - left). Therefore, we only need 2 state variables: \text{i}i and \text{left}left, and we can calculate \text{right}right inside the function.

Now that we have our state variables, what should our function return? The problem is asking for the maximum score from some number of operations, so let's have our function \text{dp(i, left)}dp(i, left) return the maximum possible score if we have already done \text{i}i total operations and used \text{left}left numbers from the left side. To answer the original problem, we should return \text{dp(0, 0)}dp(0, 0).

\2.A **recurrence relation** to transition between states

At each state, we have to perform an operation. As stated in the problem description, we need to decide whether to take from the left end (\text{nums[left]}nums[left]) or the right end (\text{nums[right]}nums[right]) of the current \text{nums}nums. Then we need to multiply the number we choose by \text{multipliers[i]}multipliers[i], add this value to our score, and finally remove the number we chose from \text{nums}nums. For implementation purposes, "removing" a number from \text{nums}nums means incrementing our state variables \text{i}i and \text{left}left so that they point to the next two left and right numbers.

Let \text{mult} = \text{multipliers[i]}mult=multipliers[i] and \text{right = nums.length - 1 - (i - left)}right = nums.length - 1 - (i - left). The only decision we have to make is whether to take from the left or right of \text{nums}nums.

- If we choose left, we gain \text{mult} \cdot \text{nums[left]}mult⋅nums[left] points from this operation. Then, the next operation will occur at \text{(i + 1, left + 1)}(i + 1, left + 1). \text{i}i gets incremented at every operation because it represents how many operations we have done, and \text{left}left gets incremented because it represents how many left operations we have done. Therefore, our total score is \text{mult} \cdot \text{nums[left] + dp(i + 1, left + 1)}mult⋅nums[left] + dp(i + 1, left + 1).
- If we choose right, we gain \text{mult} \cdot \text{nums[right]}mult⋅nums[right] points from this operation. Then, the next operation will occur at \text{(i + 1, left)}(i + 1, left). Therefore, our total score is \text{mult} \cdot \text{nums[right] + dp(i + 1, left)}mult⋅nums[right] + dp(i + 1, left).

Since we want to maximize our score, we should choose the side that gives more points. This gives us our recurrence relation:

\text{dp(i, left)} = \max(\text{mult} \cdot \text{nums[left]} + \text{dp(i + 1, left + 1)}, \text{ mult} \cdot \text{nums[right]} + \text{dp(i + 1, left)})dp(i, left)=max(mult⋅nums[left]+dp(i + 1, left + 1), mult⋅nums[right]+dp(i + 1, left))

Where \text{mult} \cdot \text{nums[left]} + \text{dp(i + 1, left + 1)}mult⋅nums[left]+dp(i + 1, left + 1) represents the points we gain by taking from the left end of \text{nums}nums plus the maximum points we can get from the remaining \text{nums}nums array and \text{mult} \cdot \text{nums[right]} + \text{dp(i + 1, left)}mult⋅nums[right]+dp(i + 1, left) represents the points we gain by taking from the right end of \text{nums}nums plus the maximum points we can get from the remaining \text{nums}nums array.

\3. **Base cases**

The problem statement says that we need to perform \text{m}m operations. When \text{i}i equals \text{m}m, that means we have no operations left. Therefore, we should return \text{0}0.



### Top-down Implementation

Let's put the 3 parts of the framework together for a solution to the problem.

Protip: for Python, the [functools](https://docs.python.org/3/library/functools.html) module provides super handy tools that automatically memoize a function for us. We're going to use the `@lru_cache` decorator in the Python implementation.

> If you find yourself needing to memoize a function in an interview and you're using Python, check with your interviewer if using modules like functools is OK.

This particular problem happens to have very tight time limits. For Java, instead of using a hashmap for the memoization, we will use a 2D array. For Python, we're going to limit our cache size to \text{2000}2000.

```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # lru_cache from functools automatically memoizes the function
        @lru_cache(2000)
        def dp(i, left):
            # Base case
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)
            
            # Recurrence relation
            return max(mult * nums[left] + dp(i + 1, left + 1), 
                       mult * nums[right] + dp(i + 1, left))
                       
        n, m = len(nums), len(multipliers)
        return dp(0, 0)
```





### Bottom-up Implementation

In the bottom-up implementation, the array works the same way as the function from top-down. \text{dp[i][left]}dp[i][left] represents the max score possible if \text{i}i operations have been performed and \text{left}left left operations have been performed.

Earlier in the explore card, we learned that while bottom-up is typically faster than top-down, it is often harder to implement. This is because the order in which we iterate needs to be precise. You'll see in the implementations below that we use the same math to calculate \text{right}right, and the same recurrence relation but we need to iterate backwards starting from \text{m}m (because the base case happens when \text{i}i equals \text{m}m). We also need to initialize \text{dp}dp with one extra row so that we don't go out of bounds in the first iteration of the outer loop.

```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], 
                                  mult * nums[right] + dp[i + 1][left])        
        return dp[0][0]
```