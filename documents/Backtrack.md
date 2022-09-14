# 一看就懂，一写就懵？搞懂回溯算法，一口气刷了20多道题

# 一、回溯算法

## 1.1什么是回溯？

回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。——摘自《百度百科》![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdbc71a154d74fc585a5df8cd2c3ed6d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

**1.1 一般步骤：**

1. 针对所给问题，定义问题的解空间，它至少包含问题的一个（最优）解。
2. 确定易于搜索的解空间结构,使得能用回溯法方便地搜索整个解空间 。
3. 以深度优先的方式搜索解空间，并且在搜索过程中用剪枝函数避免无效搜索。

**1.2 如何理解回溯算法？**

1. 为问题建立解空间结构
2. 在解空间结构上进行DFS搜索
3. 设立回溯出口和剪枝点，减少无效搜索，出口处保存有效解.

**1.3 解决那些问题？**

1. 组合问题：N个数⾥⾯按⼀定规则找出k个数的集合
2. 切割问题：⼀个字符串按⼀定规则有⼏种切割⽅式
3. ⼦集问题：⼀个N个数的集合⾥有多少符合条件的⼦集
4. 排列问题：N个数按⼀定规则全排列，有⼏种排列⽅式
5. 棋盘问题：N皇后，解数独等等。

**1.4递归与回溯**

首先先说明一下对递归 (Recursive)与回溯 (Backtrack)的理解。

**1.4.1 递归 (Recursive)**

程序调用自身的编程技巧称为递归。 递归做为一种算法在程序设计语言中广泛应用。 一个过程或函数在其定义或说明中有直接或间接调用自身的一种方法，它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量。 ——摘自《百度百科》

通常来说，为了描述问题的某一状态，必须用到该状态的上一个状态；而如果要描述上一个状态，又必须用到上一个状态的上一个状态…… 这样用自己来定义自己的方法就是递归。

**1.4.2. 回溯 (Backtrack)**

回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。 ——摘自《百度百科》

在这种思想下，我们需要清晰的找出三个要素：选择 (Options)，限制 (Restraints)，结束条件 (Termination)。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/788cd990e86f4279980a14e467c920de~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

**1.5.递归与回溯的区别**

递归是一种算法结构。递归会出现在子程序中，形式上表现为直接或间接的自己调用自己。典型的例子是阶乘，计算规律为：n!=n×(n−1)!n!=n \times (n-1)!，基本如下所示：

```js
let fac = (n)=> {
    if(n == 1){
       return n;
    }else{
      return (n*fac(n - 1)); 
    }    
}
复制代码
```

回溯是一种算法思想，它是用递归实现的。回溯的过程类似于穷举法，但回溯有“剪枝”功能，即自我判断过程。

**二、Leetcode回溯题目**

**2.1- 22. 括号生成**

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

```js
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
复制代码
```

示例 2：

```js
输入：n = 1
输出：["()"]
复制代码
```

提示： 1 <= n <= 8

思路分析

1. 判断左右括号所剩的数量，最初始都是n;当左括号（(）有剩余，继续做选择；
2. 判断当右括号比左括号剩的多，才能选右括号；继续递归做选择
3. 出口:构建的字符串是 2n的时候，此时已经该分支已经构建完成，加入选项；

简答绘制图形

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/574675e16b23475cb29aaff86d4c3a17~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

解题代码

```js
var generateParenthesis = function (n) {
    const res = [];
    const backTracing = (lRemain, rRemain, str) => { // 左右括号所剩的数量，str是当前构建的字符串
        if (str.length == 2 * n) { // 字符串构建完成
            res.push(str);           // 加入解集
            return;                  // 结束当前递归分支
        }
        if (lRemain > 0) {         // 只要左括号有剩，就可以选它，然后继续做选择（递归）
            backTracing(lRemain - 1, rRemain, str + "(");
        }
        if (lRemain < rRemain) {   // 右括号比左括号剩的多，才能选右括号
            backTracing(lRemain, rRemain - 1, str + ")"); // 然后继续做选择（递归）
        }
    };
    backTracing(n, n, ""); // 递归的入口，剩余数量都是n，初始字符串是空串
    return res;
};
复制代码
```

**2.2 - 46. 全排列**

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

```js
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
复制代码
```

示例 2：

```js
输入：nums = [0,1]
输出：[[0,1],[1,0]]
复制代码
```

示例 3：

```js
输入：nums = [1]
输出：[[1]]
复制代码
```

提示： 1 <= nums.length <= 6 -10 <= nums[i] <= 10 nums 中的所有整数 互不相同

解题思路

1. 回溯终止条件：该条路径长度与达到nums长度；
2. 加入当前值到路径，如果结果里面已经包含这个路径，则不加入结果里面，否则继续选择这个选项；

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8130c056516043089a27244655db0e25~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

解题代码

```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
    if (!nums.length) return
    let res = []
    let backTrack = path => {
        //长度满足条件，加入结果
        if (path.length === nums.length) {
            res.push(path)
            return
        }
        nums.forEach(item => {
            if (path.includes(item)) return //不包含重复的数字
            backTrack([...path, item]) //加入路径，继续递归选择
        });
    }
    backTrack([])
    return res
};

复制代码
```

**2.3 - n 皇后问题**

研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。***

![image](https://upload-images.jianshu.io/upload_images/23849911-018ba83744b413ee.image?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

皇后走法规则

皇后的走法是：可以横直斜走，格数不限。因此要求皇后彼此之间不能相互攻击，等价于要求任何两个皇后都不能在同一行、同一列以及同一条斜线上。

示例

示例 1：![image](https://upload-images.jianshu.io/upload_images/23849911-14b9bee8aba2ddd4.image?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```js
输入：n = 4
输出：2
复制代码
```

解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：

```js
输入：n = 1
输出：1
复制代码
```

提示： 1 <= n <= 9

解题思路

1. 定义判断当前位置的检验函数，约束条件包含 ，不能同行，不能同列，不能同对角线（45度和135度）
2. 定义棋盘；标准回溯处理；

使用回溯的具体做法是：依次在每一行放置一个皇后，每次新放置的皇后都不能和已经放置的皇后之间有攻击，即新放置的皇后不能和任何一个已经放置的皇后在同一列以及同一条斜线上。当 NNN 个皇后都放置完毕，则找到一个可能的解，将可能的解的数量加 111。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd09da254e2a4b6d9fd9ece951486e98~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

[图片来源](https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_37763204%2Farticle%2Fdetails%2F79519671)

解题代码

```js
var totalNQueens = function (n) {
    let count = 0; //皇后可放置的总数
    let isValid = (row, col, board, n) => {
        //所在行不用判断，每次都会下移一行
        //判断同一列的数据是否包含
        for (let i = 0; i < row; i++) {
            if (board[i][col] === 'Q') {
                return false
            }
        }
        //判断45度对角线是否包含
        for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] === 'Q') {
                return false
            }
        }
        //判断135度对角线是否包含
        for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; j--, i--) {
            if (board[i][j] === 'Q') {
                return false
            }
        }
        return true
    }

    let backTracing = (row, board) => {
        //走到最后一行，统计次数
        if (row === n) {
            count++;
            return
        }

        for (let x = 0; x < n; x++) {
            //判断该位置是否可以放置 皇后
            if (isValid(row, x, board, n)) {
                board[row][x] = 'Q'; //放置皇后
                backTracing(row + 1, board); //递归
                board[row][x] = '.'; //回溯，撤销处理结果
            }
        }
    }
    backTracing(0, board)
    let board = [...Array(n)].map(v => v = ([...Array(n)]).fill('.')) //棋盘
    return count
};
复制代码
```

**2.4 - 78. 子集**

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：

```js
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
复制代码
```

示例 2：

```js
输入：nums = [0]
输出：[[],[0]]
复制代码
```

提示： 1 <= nums.length <= 10 -10 <= nums[i] <= 10 nums 中的所有元素 互不相同

解题思路

1. 枚举出所有可选的数；加入选项；
2. 撤销加入的选项，将选项加入结果

解题代码

```js
const subsets = (nums) => {
    const res = [];
    const backTracing = (index, list) => {
        res.push(list.slice());     // 调用子递归前，加入解集
        for (let i = index; i < nums.length; i++) { // 枚举出所有可选的数
            list.push(nums[i]);       // 选这个数
            backTracing(i + 1, list);         // 基于选这个数，继续递归
            list.pop();               // 撤销选这个数
        }
    };
    backTracing(0, []);
    return res;
};
复制代码
```

**2.5 - 77. 组合**

给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：

```js
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
复制代码
```

示例 2：

```js
输入：n = 1, k = 1
输出：[[1]]
复制代码
```

提示： 1 <= n <= 20 1 <= k <= n

解题思路

1. 枚举出所有可选的数；加入选项；
2. 撤销加入的选项，将选项加入结果
3. 剪枝条件:选项的长度满足条件；

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0fed7e92d3449c0aa28e573f4ac4138~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

解题代码

```js
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
    let result = [];
    let backTracing = (start, path) => {
        // 如果已经选满了的话，加入结果集中
        if (path.length == k) {
            result.push(path.slice());
            return;
        }
        // 从开始的数字到末尾的数字
        for (let i = start; i <= n; i++) {
            // 加入选择列表中
            path.push(i);
            // 继续深度搜索
            backTracing(i + 1, path);
            // 撤销选择
            path.pop(i);
        }
    };
    backTracing(1, []);
    return result;
};
复制代码
```

**2.6 - 081. 允许重复选择元素的组合**

给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

示例 1：

```js
输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
复制代码
```

示例 2：

```js
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
复制代码
```

示例 3：

```js
输入: candidates = [2], target = 1
输出: []
复制代码
```

示例 4：

```js
输入: candidates = [1], target = 1
输出: [[1]]
复制代码
```

示例 5：

```js
输入: candidates = [1], target = 2
输出: [[1,1]]
复制代码
```

提示： 1 <= candidates.length <= 30 1 <= candidates[i] <= 200 candidate 中的每个元素都是独一无二的。 1 <= target <= 500

解题思路

1. 将当前元素加入到选项里面，并将计算结果，传到选项，继续递归；
2. 当选项和大于目标值时，结束这个选项，直到找到符合的选项，并将选项加入结果；

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94816a5d728c45688526a3bf2e692a5d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

解题代码

```js
var combinationSum = function (candidates, target) {
    const result = [], visited = [];
    backTracing(0, 0);
    return result;

    function backTracing(sum, cur) {
        if (target === sum) result.push(visited.slice());
        if (target <= sum) return;
        for (let i = cur; i < candidates.length; i++) {
            visited.push(candidates[i]); //加入到选项里面
            backTracing(sum + candidates[i], i);//选择这个选项，继续递归
            visited.pop(); //插销这个选择
        }
    }
};
复制代码
```

**2.7 - 216. 组合总和 III**

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明： 所有数字都是正整数。 解集不能包含重复的组合。

示例 1:

```js
输入: k = 3, n = 7
输出: [[1,2,4]]
复制代码
```

示例 2:

```js
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
复制代码
```

解题思路

同组合1

解题代码

```js
var combinationSum3 = function (k, n) {
    let ans = [];
    let backTracing = (start, path) => {
        if (path.length === k && path.reduce((acc, prev) => acc += prev) === n) {
            ans.push(path.slice())
            return
        }
        for (let i = start; i <= 9; i++) {
            path.push(i)
            backTracing(i + 1, path)
            path.pop(i)
        }
    }
    backTracing(1, [])
    return ans
};
复制代码
```

**2.8 - 17. 电话号码的字母组合**

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91285e87168643b8ae19866b16438eaf~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

示例 1：

```js
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
复制代码
```

示例 2：

```js
输入：digits = ""
输出：[]
复制代码
```

示例 3：

```js
输入：digits = "2"
输出：["a","b","c"]
复制代码
```

提示： 0 <= digits.length <= 4 digits[i] 是范围 ['2', '9'] 的一个数字。

解题思路

1. 找到当前按钮对应的字母字符串
2. 拼接按钮对应的字符串组合
3. 选项满足长度，加入结果

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91fbe6f9d8f44ddba5dd9956697ee945~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp)

解题代码

```js
var letterCombinations = function (digits) {
    if(!digits.length) return []
    const dic = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz',
    }, ans = [];

    let backTracing = (cur, index) => {
        if (index > digits.length - 1) { //选项满足长度，加入结果
            ans.push(cur)
            return
        }
        let curDic = dic[digits[index]] //找到当前按钮对应的字母字符串
        for (let prop of curDic) {
            backTracing(cur + prop,index+1) //拼接按钮对应的字符串组合
        }
    }
    backTracing('', 0)
    return ans
};
复制代码
```

**2.9 - 08.01. 三步问题**

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

```js
 输入：n = 3 
 输出：4
 说明: 有四种走法
复制代码
```

示例2:

```js
 输入：n = 5
 输出：13
复制代码
```

提示: n范围在[1, 1000000]之间

解题代码(会超时)

```js
 var waysToStep = function (n) {
    let ans = [], map = [1, 2, 3]
    let backTracing = (path, sum) => {
        if (sum >= n) {
            if (sum == n) {
                ans++;
            }
            return
        }
        for (let i = 0; i < 3; i++) {
            path.push(map[i]);
            backTracing(path, sum + map[i])
            path.pop(i)
        }
    }
    backTracing([], 0)
    return ans
};
复制代码
```

动态规划解法

```js
/**
 * @param {number} n
 * @return {number}
 */
var waysToStep = function (n) {
    let dp =[],mod = 1000000007;
    dp[0]=0,dp[1]=1,dp[2]=2,dp[3]=4;
    for (let i = 4; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
    }
    return dp[n]
};
复制代码
```

**2-10 - 40. 组合总和 II**

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。 注意：解集不能包含重复的组合。

示例 1:

```js
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
复制代码
```

示例 2:

```js
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
复制代码
```

提示: 1 <= candidates.length <= 100 1 <= candidates[i] <= 50 1 <= target <= 30

解题思路

思路同组合1

解题代码

```js
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
 var combinationSum2 = function (candidates, target) {
    candidates.sort((a,b)=>a-b)
    let ans = [];
    let backTracing = (start, path, sum) => {
        if (sum >= target) {
            if (sum === target) {
                ans.push(path.slice())
            }
            return
        }
        for (let i = start; i < candidates.length; i++) {
            if (i - 1 >= start && candidates[i - 1] == candidates[i]) {
                continue;
            }
            path.push(candidates[i])
            backTracing(i + 1, path, sum + candidates[i])
            path.pop()
        }
    }
    backTracing(0, [], 0)
    return ans
};
复制代码
```

**2-11 - 47. 全排列 II**

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

```js
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
复制代码
```

示例 2：

```js
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
复制代码
```

提示： 1 <= nums.length <= 8 -10 <= nums[i] <= 10

解题思路

同上全排列

解题代码

```js
var permuteUnique = function (nums) {
   let ans = [];
   let used = Array(nums.length).fill(false)
   let backTracing = (start, path) => {
       if (start === nums.length) {
           ans.push(path.slice())
           return
       }
       for (let i = 0; i < nums.length; ++i) {
           if (used[i] || (i > 0 && nums[i] === nums[i - 1] && !used[i - 1])) {
               continue;
           }
           path.push(nums[i])
           used[i] = true
           backTracing(start + 1, path)
           used[i] = false
           path.pop()
       }
   }
   nums.sort((a, b) => a - b)
   backTracing(0, [])
   return ans

};
复制代码
```

**三、总结**

主要运用了回溯算法；而解决一个回溯问题，实际上就是一个决策树的遍历过程。

3.1 模板

```js
let backtracking=(路径，选择列表) =>{
    if (满足结束条件)) {
        存放路径;
        return;
    }
    for (选择：路径，选择列表) {
        做出选择；
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
复制代码
```

即:

1. 1.路径：也就是已经做出的选择。
2. 2.选择列表：也就是你当前可以做的选择。
3. 3.结束条件：也就是到达决策树底层，无法再做选择的条件。

3.2 剪枝函数

1. 1.用约束条件剪除得不到的可行解的子树
2. 2.用目标函数剪取得不到的最优解的子树

3.3 回溯法的一般步骤：

1. 1.设置初始化的方案（给变量赋初始值，读入已知数据等）
2. 2.变换方式去试探，若全部试完侧转（7）
3. 3.判断此法是否成功（通过约束函数），不成功则转（2）
4. 4.试探成功则前进一步再试探
5. 5.正确方案还是未找到则转（2）
6. 6.以找到一种方案则记录并打印
7. 7.退回一步（回溯），若未退到头则转（2）
8. 8.已退到头则结束或打印无解

继续加油！！！

**四、参考文献**

1. LeetCode 刷题笔记——递归与回溯的理解[LeetCode 刷题笔记——递归与回溯的理解](https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1434886)
2. 图解回溯算法[图解回溯算法](https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fgui951753%2Farticle%2Fdetails%2F108014030)
3. 回溯算法总结[回溯算法总结](https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F8fc2257d1f4e)