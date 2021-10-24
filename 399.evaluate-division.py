# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc tags=union-find;graph

# @lc imports=start
import collections
from re import X
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
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """ Solution 1: Build a graph and using the DFS to traverse the graph """
        # graph = defaultdict(defaultdict)
        # # use DFS to traverse the graph

        # def graph_helper(graph, src, dst, acc_product, visited):
        #     visited.add(src)
        #     ret = - 1.0
        #     neighbors = graph[src]
        #     if dst in neighbors:
        #         ret = acc_product * neighbors[dst]
        #     else:
        #         for neighbor, value in neighbors.items():
        #             if neighbor in visited:
        #                 continue
        #             ret = graph_helper(graph, neighbor, dst,
        #                                acc_product*value, visited)
        #             if ret != -1.0:
        #                 break
        #     # visited.remove(src)
        #     return ret

        # # building the undirected graph from equation and values
        # # we need to store the both direction link
        # for (dividend, divisor), value in zip(equations, values):
        #     graph[dividend][divisor] = value
        #     graph[divisor][dividend] = 1.0 / value

        # output = []
        # for dividend, divisor in queries:
        #     if dividend not in graph or divisor not in graph:
        #         ret = -1.0
        #     elif dividend == divisor:
        #         ret = 1.0
        #     else:
        #         visited = set()
        #         ret = graph_helper(graph, dividend, divisor, 1, visited)
        #     output.append(ret)
        # return output

        """ Solution 2: Use a Union-Find data structure """
        # here we will be using a union find data structure
        # but this union find data structure would be customized one since we 
        # will store the element in a foramt of {'nodeId': (node_group, weight) }
        uf_root = {} # each element has nodeid: node_group, weight
        def find(node_id):
            if node_id not in uf_root:
                uf_root[node_id] = (node_id, 1)
                       
            groupId, node_weight = uf_root[node_id]
            if groupId != node_id:
                
                new_groupId, group_weight = find(groupId)
                # do not forget to update the weight
                uf_root[node_id] = (new_groupId, node_weight * group_weight)
            return uf_root[node_id]

        def union(dividend, divisor, value):
            dividend_groupId, dividend_weight = find(dividend)
            divisor_groupId, divisor_weight = find(divisor)
            if dividend_groupId != divisor_groupId:
                # merge the two groupd together
                uf_root[dividend_groupId] = (
                    divisor_groupId, divisor_weight * value / dividend_weight)
        
        # build the union find data structure
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)
        
        results = []
        # now go through the queries
        for (dividend, divisor) in queries:
            # if both dividend and divisor not in union find data structure
            # we return -1
            if dividend not in uf_root or divisor not in uf_root:
                results.append(-1.0)
            else:
                dividend_groupId, dividend_weight = find(dividend)
                divisor_groupId, divisor_weight = find(divisor)
                # if they belong to the saem group
                if dividend_groupId == divisor_groupId:
                    results.append(dividend_weight / divisor_weight)
                else:
                    results.append(-1.0)
        return results






# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]')
    print('Exception :')
    print('[6.00000,0.50000,-1.00000,1.00000,-1.00000]')
    print('Output :')
    print(str(Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [
          ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]')
    print('Exception :')
    print('[3.75000,0.40000,5.00000,0.20000]')
    print('Output :')
    print(str(Solution().calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [
          1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'equations = [["a","b"]], values = [0.5], queries =[["a","b"],["b","a"],["a","c"],["x","y"]]')
    print('Exception :')
    print('[0.50000,2.00000,-1.00000,-1.00000]')
    print('Output :')
    print(str(Solution().calcEquation([["a", "b"]], [0.5], [
          ["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])))
    print()

    pass
# @lc main=end
