# @lc app=leetcode id=1766 lang=python3
#
# [1766] Tree of Coprimes
#


# @lc tags=Unknown

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
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        """ Solution 1 """
#         n = len(nums)
#         def gcd(x, y):
#             while y:
#                 x, y = y, x%y
#             return x

#         graph = collections.defaultdict(list)

#         coprimes = collections.defaultdict(list)

#         latest_node = [-1] * 51

#         depth = [0] * n

#         for x, y in edges:
#             graph[x].append(y)
#             graph[y].append(x)

#         for i in range(1, 51):
#             for j in range(1, 51):
#                 if gcd(i, j) == 1:
#                     coprimes[i].append(j)

#         ans = [-1] * n

#         # dfs,遍历当前节点的质数表,更新其最大深度即可
#         def dfs(cur, par):
#             for prime in coprimes[nums[cur]]:

#                 # 若当前质数还未出现
#                 if latest_node[prime] == -1:
#                     continue

#                 # 若当前节点未记录祖先节点或当前深度大于其记录节点深度,进行更新
#                 if ans[cur] == -1 or depth[ans[cur]] < depth[latest_node[prime]]:
#                     ans[cur] = latest_node[prime]

#             # 保存该节点遍历前的最近出现节点
#             temp = latest_node[nums[cur]]

#             # 更新当前质数出现节点
#             latest_node[nums[cur]] = cur

#             for next_node in graph[cur]:
#                 if next_node != par:
#                     # 更新深度
#                     depth[cur] = depth[par] + 1
#                     dfs(next_node,cur)

#             latest_node[nums[cur]] = temp
#             return

#         dfs(0,-1)
#         return ans

        """ Solution 2 """
        def computeGCD(x, y):
            while(y):
                x, y = y, x % y
            return x
        
        # fixed cost precomputed GCD data
        dm = {i:{j for j in range(51) if computeGCD(i,j) == 1} for i in range(51)}
        
        ed = defaultdict(list)
        ans = [-1]*len(nums)
        for x,y in edges:
            ed[x].append(y)
            ed[y].append(x)
        
        done = set()
        stack = deque([(0,{})])
        lvl = 0 # keep track of ordering of parents
        while stack:
            sl = len(stack)
            for _ in range(sl):
                node, parents  = stack.popleft()
                overlap = dm[nums[node]] & parents.keys()
                if overlap:
                    # we only need the most recent parent (max lvl value) out of the overlap
                    ans[node] = parents[max(overlap, key=lambda x: parents[x][1])][0]
                done.add(node)
                for child in ed[node]:
                    if child not in done:
                        np = parents.copy()
                        np[nums[node]] = (node, lvl)
                        stack.append((child, np ))
            lvl += 1
            
        return ans

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]')
    print('Exception :')
    print('[-1,0,0,1]')
    print('Output :')
    print(str(Solution().getCoprimes([2,3,3,2],[[0,1],[1,2],[1,3]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [5,6,10,2,3,6,15], edges =[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]')
    print('Exception :')
    print('[-1,0,-1,0,0,0,-1]')
    print('Output :')
    print(str(Solution().getCoprimes([5,6,10,2,3,6,15],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])))
    print()
    
    pass
# @lc main=end
