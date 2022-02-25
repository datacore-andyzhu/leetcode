# dd大牛的《背包九讲》

## 1. 01背包问题

### 1.1 题目

有 ![[公式]](https://www.zhihu.com/equation?tex=N) 件物品和一个容量为 ![[公式]](https://www.zhihu.com/equation?tex=V) 的背包。第 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品的费用是 ![[公式]](https://www.zhihu.com/equation?tex=c%5Bi%5D) ，价值是 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D) 。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

### 1.2 基本思路

这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。

用子问题定义状态：即 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 表示前 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品恰放入一个容量为 ![[公式]](https://www.zhihu.com/equation?tex=v) 的背包可以获得的最大价值。则其状态转移方程便是： ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%5Cmax+%5C%7Bf%5Bi-1%5D%5Bv%5D%2C~f%5Bi-1%5D%5Bv-c%5Bi%5D%5D%2Bw%5Bi%5D%5C%7D) 。

这个方程非常重要，基本上所有跟背包相关的问题的方程都是由它衍生出来的。所以有必要将它详细解释一下：“将前 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品放入容量为 ![[公式]](https://www.zhihu.com/equation?tex=v) 的背包中”这个子问题，若只考虑第 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品的策略（放或不放），那么就可以转化为一个只牵扯前 ![[公式]](https://www.zhihu.com/equation?tex=i-1) 件物品的问题。如果不放第 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品，那么问题就转化为“前 ![[公式]](https://www.zhihu.com/equation?tex=i-1) 件物品放入容量为v的背包中”；如果放第 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品，那么问题就转化为“前 ![[公式]](https://www.zhihu.com/equation?tex=i-1) 件物品放入剩下的容量为 ![[公式]](https://www.zhihu.com/equation?tex=v-c%5Bi%5D) 的背包中”，此时能获得的最大价值就是 ![[公式]](https://www.zhihu.com/equation?tex=f+%5Bi-1%5D%5Bv-c%5Bi%5D%5D) 再加上通过放入第i件物品获得的价值 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D) 。

注意 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 有意义当且仅当存在一个前i件物品的子集，其费用总和为 ![[公式]](https://www.zhihu.com/equation?tex=v) 。所以按照这个方程递推完毕后，最终的答案并不一定是 ![[公式]](https://www.zhihu.com/equation?tex=f%5BN%5D+%5BV%5D) ，而是 ![[公式]](https://www.zhihu.com/equation?tex=f%5BN%5D%5B0...V%5D) 的最大值。如果将状态的定义中的“恰”字去掉，在转移方程中就要再加入一项 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv-1%5D) ，这样就可以保证 ![[公式]](https://www.zhihu.com/equation?tex=f%5BN%5D+%5BV%5D) 就是最后的答案。至于为什么这样就可以，由你自己来体会了。

### 1.3 优化空间复杂度

以上方法的时间和空间复杂度均为 ![[公式]](https://www.zhihu.com/equation?tex=O%28N%2AV%29) ，其中时间复杂度基本已经不能再优化了，但空间复杂度却可以优化到 ![[公式]](https://www.zhihu.com/equation?tex=O%28V%29) 。

先考虑上面讲的基本思路如何实现，肯定是有一个主循环 ![[公式]](https://www.zhihu.com/equation?tex=i%3D1...N) ，每次算出来二维数组 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5B0...V%5D) 的所有值。那么，如果只用一个数组 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5B0..V%5D) ，能不能保证第 ![[公式]](https://www.zhihu.com/equation?tex=i) 次循环结束后f[v]中表示的就是我们定义的状态 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 呢？ ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 是由 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi-1%5D%5Bv%5D) 和 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi-1%5D+%5Bv-c%5Bi%5D%5D) 两个子问题递推而来，能否保证在推 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 时（也即在第i次主循环中推 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bv%5D) 时）能够得到 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi-1%5D%5Bv%5D) 和 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi-1%5D%5Bv+-c%5Bi%5D%5D) 的值呢？事实上，这要求在每次主循环中我们以 ![[公式]](https://www.zhihu.com/equation?tex=v%3DV..0) 的顺序推 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bv%5D) ，这样才能保证推 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bv%5D) 时 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bv-c%5Bi%5D%5D) 保存的是状态 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi+-1%5D%5Bv-c%5Bi%5D%5D) 的值。伪代码如下：

```cpp
for i=1..N
    for v=V..0
        f[v]=max{f[v],f[v-c[i]]+w[i]};
```

其中的 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bv%5D%3Dmax%7Bf%5Bv%5D%2Cf%5Bv-c%5Bi%5D%5D%7D) 一句恰就相当于我们的转移方程 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%5Cmax%5C%7Bf%5Bi-1%5D%5Bv%5D%2C~f%5Bi-+1%5D%5Bv-c%5Bi%5D%5D%5C%7D) ，因为现在的 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bv-c%5Bi%5D%5D) 就相当于原来的 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi-1%5D%5Bv-c%5Bi%5D%5D) 。如果将v的循环顺序从上面的逆序改成顺序的话，那么则成了 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 由 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv-c%5Bi%5D%5D) 推知，与本题意不符，但它却是另一个重要的背包问题（完全背包）最简捷的解决方案，故学习只用一维数组解01背包问题是十分必要的。

### 1.4 相关题目

[2. 01背包问题 - AcWing题库www.acwing.com/problem/content/2/](https://link.zhihu.com/?target=https%3A//www.acwing.com/problem/content/2/)

代码：

```cpp
#include<iostream>
using namespace std;

const int N = 1010;

int v[N], w[N], dp[N];//dp[N][N]

int main(){
    int n, m;    
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> v[i] >> w[i];
    }
    
    for(int i = 1; i <= n; i++){
        // for(int j = 0; j <= m; j++){
        //     if(j < v[i])
        //         dp[i][j] = dp[i-1][j];
        //     else
        //         dp[i][j]=max(dp[i-1][j], dp[i-1][j-v[i]]+w[i]);
        // }
        
        for(int j = m; j >=v[i]; j--){
            dp[j] = max(dp[j], dp[j-v[i]]+w[i]);
        }
    }
    cout<<dp[m]<<endl;;
    return 0;
}
```

### 1.5 总结

01背包问题是最基本的背包问题，它包含了背包问题中设计状态、方程的最基本思想，另外，别的类型的背包问题往往也可以转换成01背包问题求解。故一定要仔细体会上面基本思路的得出方法，状态转移方程的意义，以及最后怎样优化的空间复杂度。

## 2. 完全背包问题

### 2.1 题目

有 ![[公式]](https://www.zhihu.com/equation?tex=N) 种物品和一个容量为 ![[公式]](https://www.zhihu.com/equation?tex=V) 的背包，每种物品都有无限件可用。第i种物品的费用是 ![[公式]](https://www.zhihu.com/equation?tex=c%5Bi%5D) ，价值是 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D) 。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

### 2.2 基本思路

这个问题非常类似于01背包问题，所不同的是每种物品有无限件。也就是从每种物品的角度考虑，与它相关的策略已并非取或不取两种，而是有取0件、取1件、取2件……等很多种。如果仍然按照解01背包时的思路，令 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 表示前i种物品恰放入一个容量为 ![[公式]](https://www.zhihu.com/equation?tex=v) 的背包的最大权值。仍然可以按照每种物品不同的策略写出状态转移方程，像这样： ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%5Cmax%5C%7Bf%5Bi-1%5D%5Bv-k%2Ac%5Bi%5D%5D%2Bk%2Aw%5Bi%5D%2C~~0%3C%3Dk%2Ac%5Bi%5D%3C%3D+v%5C%7D) 。这跟01背包问题一样有 ![[公式]](https://www.zhihu.com/equation?tex=O%28N%2AV%29) 个状态需要求解，但求解每个状态的时间则不是常数了，求解状态 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 的时间是 ![[公式]](https://www.zhihu.com/equation?tex=O%28v%2Fc%5Bi%5D%29) ，总的复杂度是超过 ![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 的。

将01背包问题的基本思路加以改进，得到了这样一个清晰的方法。这说明01背包问题的方程的确是很重要，可以推及其它类型的背包问题。但我们还是试图改进这个复杂度。

一个简单有效的优化

完全背包问题有一个很简单有效的优化，是这样的：若两件物品 ![[公式]](https://www.zhihu.com/equation?tex=i) 、 ![[公式]](https://www.zhihu.com/equation?tex=j) 满足c ![[公式]](https://www.zhihu.com/equation?tex=%5Bi%5D%3C%3Dc%5Bj%5D) 且 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D%3E%3Dw%5Bj%5D) ，则将物品 ![[公式]](https://www.zhihu.com/equation?tex=j) 去掉，不用考虑。这个优化的正确性显然：任何情况下都可将价值小费用高得 ![[公式]](https://www.zhihu.com/equation?tex=j) 换成物美价廉的 ![[公式]](https://www.zhihu.com/equation?tex=i) ，得到至少不会更差的方案。对于随机生成的数据，这个方法往往会大大减少物品的件数，从而加快速度。然而这个并不能改善最坏情况的复杂度，因为有可能特别设计的数据可以一件物品也去不掉。

转化为01背包问题求解

既然01背包问题是最基本的背包问题，那么我们可以考虑把完全背包问题转化为01背包问题来解。最简单的想法是，考虑到第 ![[公式]](https://www.zhihu.com/equation?tex=i) 种物品最多选 ![[公式]](https://www.zhihu.com/equation?tex=V%2Fc+%5Bi%5D) 件，于是可以把第 ![[公式]](https://www.zhihu.com/equation?tex=i) 种物品转化为 ![[公式]](https://www.zhihu.com/equation?tex=V%2Fc%5Bi%5D) 件费用及价值均不变的物品，然后求解这个01背包问题。这样完全没有改进基本思路的时间复杂度，但这毕竟给了我们将完全背包问题转化为01背包问题的思路：将一种物品拆成多件物品。

更高效的转化方法是：把第i种物品拆成费用为 ![[公式]](https://www.zhihu.com/equation?tex=c%5Bi%5D%2A2%5Ek) 、价值为 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D%2A2%5Ek) 的若干件物品，其中 ![[公式]](https://www.zhihu.com/equation?tex=k) 满足 ![[公式]](https://www.zhihu.com/equation?tex=c%5Bi%5D%2A2%5Ek%3CV) 。这是二进制的思想，因为不管最优策略选几件第 ![[公式]](https://www.zhihu.com/equation?tex=i) 种物品，总可以表示成若干个 ![[公式]](https://www.zhihu.com/equation?tex=2%5Ek) 件物品的和。这样把每种物品拆成 ![[公式]](https://www.zhihu.com/equation?tex=O%28log%28V%2Fc%5Bi%5D%29%29) 件物品，是一个很大的改进。但我们有更优的 ![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 的算法。 ![[公式]](https://www.zhihu.com/equation?tex=%2A+O%28VN%29) 的算法这个算法使用一维数组，先看伪代码：

```cpp
for i=1..N
    for v=0..V
        f[v]=max{f[v],f[v-c[i]]+w[i]};
```

你会发现，这个伪代码与01背包的伪代码只有v的循环次序不同而已。为什么这样一改就可行呢？首先想想为什么01背包中要按照 ![[公式]](https://www.zhihu.com/equation?tex=v%3DV..0) 的逆序来循环。这是因为要保证第 ![[公式]](https://www.zhihu.com/equation?tex=i) 次循环中的状态 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 是由状态 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi-1%5D%5Bv-c%5Bi%5D%5D) 递推而来。换句话说，这正是为了保证每件物品只选一次，保证在考虑“选入第 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品”这件策略时，依据的是一个绝无已经选入第 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品的子结果 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi-1%5D%5Bv-c%5Bi%5D%5D) 。而现在完全背包的特点恰是每种物品可选无限件，所以在考虑“加选一件第i种物品”这种策略时，却正需要一个可能已选入第i种物品的子结果 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv-c%5Bi%5D%5D) ，所以就可以并且必须采用 ![[公式]](https://www.zhihu.com/equation?tex=v%3D+0..V) 的顺序循环。这就是这个简单的程序为何成立的道理。

这个算法也可以以另外的思路得出。例如，基本思路中的状态转移方程可以等价地变形成这种形式： ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%5Cmax%5C%7Bf%5Bi-1%5D%5Bv%5D%2C~f%5Bi%5D%5Bv-c%5Bi%5D%5D%2Bw%5Bi%5D%5C%7D) ，将这个方程用一维数组实现，便得到了上面的伪代码。

### 2.3 总结

完全背包问题也是一个相当基础的背包问题，它有两个状态转移方程，分别在“基本思路”以及“ ![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 的算法“的小节中给出。希望你能够对这两个状态转移方程都仔细地体会，不仅记住，也要弄明白它们是怎么得出来的，最好能够自己想一种得到这些方程的方法。事实上，对每一道动态规划题目都思考其方程的意义以及如何得来，是加深对动态规划的理解、提高动态规划功力的好方法。

## 3. 多重背包问题

### 3.1 题目

有 ![[公式]](https://www.zhihu.com/equation?tex=N) 种物品和一个容量为 ![[公式]](https://www.zhihu.com/equation?tex=V) 的背包。第i种物品最多有 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D) 件可用，每件费用是 ![[公式]](https://www.zhihu.com/equation?tex=c%5Bi%5D) ，价值是 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D) 。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

### 3.2 基本算法

这题目和完全背包问题很类似。基本的方程只需将完全背包问题的方程略微一改即可，因为对于第i种物品有 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D%2B1) 种策略：取 ![[公式]](https://www.zhihu.com/equation?tex=0) 件，取 ![[公式]](https://www.zhihu.com/equation?tex=1) 件……取 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D) 件。令 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 表示前i种物品恰放入一个容量为 ![[公式]](https://www.zhihu.com/equation?tex=v) 的背包的最大权值，则： ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%5Cmax%5C%7Bf%5Bi-1%5D%5Bv-k%2Ac%5Bi%5D%5D%2B+k%2Aw%5Bi%5D~%7C~0%3C%3Dk%3C%3Dn%5Bi%5D%5C%7D) 。复杂度是 ![[公式]](https://www.zhihu.com/equation?tex=O%28V%2A+%5Csum+n%5Bi%5D%29) 。

转化为01背包问题

另一种好想好写的基本方法是转化为01背包求解：把第i种物品换成 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D) 件01背包中的物品，则得到了物品数为 ![[公式]](https://www.zhihu.com/equation?tex=%5Csum+n%5Bi%5D) 的01背包问题，直接求解，复杂度仍然是 ![[公式]](https://www.zhihu.com/equation?tex=O%28V%2A%5Csum+n%5Bi%5D%29) 。

但是我们期望将它转化为01背包问题之后能够像完全背包一样降低复杂度。仍然考虑二进制的思想，我们考虑把第i种物品换成若干件物品，使得原问题中第i种物品可取的每种策略——取 ![[公式]](https://www.zhihu.com/equation?tex=0..n%5Bi%5D) 件——均能等价于取若干件代换以后的物品。另外，取超过 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D) 件的策略必不能出现。

方法是：将第i种物品分成若干件物品，其中每件物品有一个系数，这件物品的费用和价值均是原来的费用和价值乘以这个系数。使这些系数分别为 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C4%2C...%2C2%5E%7Bk-1%7D%2Cn%5Bi%5D-2%5Ek%2B1) ，且k是满足 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D-2%5Ek%2B1%3E0) 的最大整数。例如，如果 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D) 为 ![[公式]](https://www.zhihu.com/equation?tex=13) ，就将这种物品分成系数分别为 ![[公式]](https://www.zhihu.com/equation?tex=1%2C2%2C4%2C6) 的四件物品。

分成的这几件物品的系数和为 ![[公式]](https://www.zhihu.com/equation?tex=n%5Bi%5D) ，表明不可能取多于n[i]件的第i种物品。另外这种方法也能保证对于 ![[公式]](https://www.zhihu.com/equation?tex=0..n%5Bi%5D) 间的每一个整数，均可以用若干个系数的和表示，这个证明可以分 ![[公式]](https://www.zhihu.com/equation?tex=0..2%5E%7Bk-1%7D) 和 ![[公式]](https://www.zhihu.com/equation?tex=2%5Ek..n%5Bi%5D) 两段来分别讨论得出，并不难，希望你自己思考尝试一下。

这样就将第i种物品分成了 ![[公式]](https://www.zhihu.com/equation?tex=O%28%5Clog+n%5Bi%5D%29) 种物品，将原问题转化为了复杂度为 ![[公式]](https://www.zhihu.com/equation?tex=O%28V%2A%5Csum+%5Clog+n%5Bi%5D%29) 的01背包问题，是很大的改进。

![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 的算法

多重背包问题同样有 ![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 的算法。这个算法基于基本算法的状态转移方程，但应用单调队列的方法使每个状态的值可以以均摊 ![[公式]](https://www.zhihu.com/equation?tex=O%281%29) 的时间求解。由于用单调队列优化的DP已超出了NOIP的范围，故本文不再展开讲解。我最初了解到这个方法是在楼天成的“男人八题”幻灯片上。

### 3.3 小结

这里我们看到了将一个算法的复杂度由 ![[公式]](https://www.zhihu.com/equation?tex=O%28V%2A%5Csum+n%5Bi%5D%29) 改进到 ![[公式]](https://www.zhihu.com/equation?tex=O%28V%2A%5Csum+%5Clog+n%5Bi%5D%29) 的过程，还知道了存在应用超出NOIP范围的知识的 ![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 算法。希望你特别注意“拆分物品”的思想和方法，自己证明一下它的正确性，并用尽量简洁的程序来实现。

## 4. 混合三种背包问题

### 4.1 问题

如果将前三种混合起来，也就是说，有的物品只可以取一次（01背包），有的物品可以取无限次（完全背包），有的物品可以取的次数有一个上限（多重背包）。应该怎么求解呢？

01背包与完全背包的混合

考虑到在前两种背包问题最后给出的伪代码只有一处不同，故如果只有两类物品：一类物品只能取一次，另一类物品可以取无限次，那么只需在对每个物品应用转移方程时，根据物品的类别选用顺序或逆序的循环即可，复杂度是 ![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 。伪代码如下：

```cpp
for i=1..N
    if第i件物品是01背包
        for v=V..0
            f[v]=max{f[v],f[v-c[i]]+w[i]};
    else if第i件物品是完全背包
        for v=0..V
            f[v]=max{f[v],f[v-c[i]]+w[i]};
```

再加上多重背包

如果再加上有的物品最多可以取有限次，那么原则上也可以给出 ![[公式]](https://www.zhihu.com/equation?tex=O%28VN%29) 的解法：遇到多重背包类型的物品用单调队列解即可。但如果不考虑超过NOIP范围的算法的话，用多重背包中将每个这类物品分成 ![[公式]](https://www.zhihu.com/equation?tex=O%28%5Clog+n%5Bi%5D%29) 个01背包的物品的方法也已经很优了。

### 4.2 小结

有人说，困难的题目都是由简单的题目叠加而来的。这句话是否公理暂且存之不论，但它在本讲中已经得到了充分的体现。本来01背包、完全背包、多重背包都不是什么难题，但将它们简单地组合起来以后就得到了这样一道一定能吓倒不少人的题目。但只要基础扎实，领会三种基本背包问题的思想，就可以做到把困难的题目拆分成简单的题目来解决。

## 5. 二维费用的背包问题

### 5.1 问题

二维费用的背包问题是指：对于每件物品，具有两种不同的费用；选择这件物品必须同时付出这两种代价；对于每种代价都有一个可付出的最大值（背包容量）。问怎样选择物品可以得到最大的价值。设这两种代价分别为代价 ![[公式]](https://www.zhihu.com/equation?tex=1) 和代价 ![[公式]](https://www.zhihu.com/equation?tex=2) ，第i件物品所需的两种代价分别为 ![[公式]](https://www.zhihu.com/equation?tex=a%5Bi%5D) 和 ![[公式]](https://www.zhihu.com/equation?tex=b%5Bi%5D) 。两种代价可付出的最大值（两种背包容量）分别为 ![[公式]](https://www.zhihu.com/equation?tex=V) 和 ![[公式]](https://www.zhihu.com/equation?tex=U) 。物品的价值为 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D) 。

### 5.2 算法

费用加了一维，只需状态也加一维即可。设 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%5Bu%5D) 表示前 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品付出两种代价分别为 ![[公式]](https://www.zhihu.com/equation?tex=v) 和 ![[公式]](https://www.zhihu.com/equation?tex=u) 时可获得的最大价值。状态转移方程就是： ![[公式]](https://www.zhihu.com/equation?tex=f+%5Bi%5D%5Bv%5D%5Bu%5D%3D%5Cmax%5C%7Bf%5Bi-1%5D%5Bv%5D%5Bu%5D~%2C~f%5Bi-1%5D%5Bv-a%5Bi%5D%5D%5Bu-b%5Bi%5D%5D%2Bw%5Bi%5D%5C%7D) 。如前述方法，可以只使用二维的数组：当每件物品只可以取一次时变量 ![[公式]](https://www.zhihu.com/equation?tex=v) 和 ![[公式]](https://www.zhihu.com/equation?tex=u) 采用顺序的循环，当物品有如完全背包问题时采用逆序的循环。当物品有如多重背包问题时拆分物品。

物品总个数的限制

有时，“二维费用”的条件是以这样一种隐含的方式给出的：最多只能取 ![[公式]](https://www.zhihu.com/equation?tex=M) 件物品。这事实上相当于每件物品多了一种“件数”的费用，每个物品的件数费用均为 ![[公式]](https://www.zhihu.com/equation?tex=1) ，可以付出的最大件数费用为 ![[公式]](https://www.zhihu.com/equation?tex=M) 。换句话说，设 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bv%5D%5Bm%5D) 表示付出费用 ![[公式]](https://www.zhihu.com/equation?tex=v) 、最多选 ![[公式]](https://www.zhihu.com/equation?tex=m) 件时可得到的最大价值，则根据物品的类型（01、完全、多重）用不同的方法循环更新，最后在 ![[公式]](https://www.zhihu.com/equation?tex=f%5B0..V%5D%5B0..M%5D) 范围内寻找答案。

另外，如果要求“恰取 ![[公式]](https://www.zhihu.com/equation?tex=M) 件物品”，则在 ![[公式]](https://www.zhihu.com/equation?tex=f%5B0..V%5D%5BM%5D) 范围内寻找答案。

### 5.3 小结

事实上，当发现由熟悉的动态规划题目变形得来的题目时，在原来的状态中加一纬以满足新的限制是一种比较通用的方法。希望你能从本讲中初步体会到这种方法。

## 6. 分组的背包问题

### 6.1 问题

有 ![[公式]](https://www.zhihu.com/equation?tex=N) 件物品和一个容量为 ![[公式]](https://www.zhihu.com/equation?tex=V) 的背包。第 ![[公式]](https://www.zhihu.com/equation?tex=i) 件物品的费用是 ![[公式]](https://www.zhihu.com/equation?tex=c%5Bi%5D) ，价值是 ![[公式]](https://www.zhihu.com/equation?tex=w%5Bi%5D) 。这些物品被划分为若干组，每组中的物品互相冲突，最多选一件。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

### 6.2 算法

这个问题变成了每组物品有若干种策略：是选择本组的某一件，还是一件都不选。也就是说设 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bk%5D%5Bv%5D) 表示前k组物品花费费用 ![[公式]](https://www.zhihu.com/equation?tex=v) 能取得的最大权值，则有 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bk%5D%5Bv%5D%3D%5Cmax%5C%7Bf%5Bk-1%5D%5Bv%5D%2Cf%5Bk-1%5D%5Bv-c%5Bi%5D%5D%2Bw%5Bi%5D~%7C~%E7%89%A9%E5%93%81i%E5%B1%9E%E4%BA%8E%E7%AC%ACk%E7%BB%84%5C%7D) 。

使用一维数组的伪代码如下：

```cpp
for所有的组k
    for所有的i属于组k
        for v=V..0
            f[v]=max{f[v],f[v-c[i]]+w[i]}
```

另外，显然可以对每组中的物品应用完全背包中“一个简单有效的优化”。

### 6.3 小结

分组的背包问题将彼此互斥的若干物品称为一个组，这建立了一个很好的模型。不少背包问题的变形都可以转化为分组的背包问题（例如 有依赖的背包问题），由分组的背包问题进一步可定义“泛化物品”的概念，十分有利于解题。

## 7. 有依赖的背包问题

### 7.1 简化的问题

这种背包问题的物品间存在某种“依赖”的关系。也就是说， ![[公式]](https://www.zhihu.com/equation?tex=i) 依赖于 ![[公式]](https://www.zhihu.com/equation?tex=j) ，表示若选物品 ![[公式]](https://www.zhihu.com/equation?tex=i) ，则必须选物品 ![[公式]](https://www.zhihu.com/equation?tex=j) 。为了简化起见，我们先设没有某个物品既依赖于别的物品，又被别的物品所依赖；另外，没有某件物品同时依赖多件物品。

### 7.2 算法

这个问题由NOIP2006金明的预算方案一题扩展而来。遵从该题的提法，将不依赖于别的物品的物品称为“主件”，依赖于某主件的物品称为“附件”。由这个问题的简化条件可知所有的物品由若干主件和依赖于每个主件的一个附件集合组成。

按照背包问题的一般思路，仅考虑一个主件和它的附件集合。可是，可用的策略非常多，包括：一个也不选，仅选择主件，选择主件后再选择一个附件，选择主件后再选择两个附件……无法用状态转移方程来表示如此多的策略。（事实上，设有 ![[公式]](https://www.zhihu.com/equation?tex=n) 个附件，则策略有 ![[公式]](https://www.zhihu.com/equation?tex=2%5E%7Bn%7D%2B1) 个，为指数级。）

考虑到所有这些策略都是互斥的（也就是说，你只能选择一种策略），所以一个主件和它的附件集合实际上对应于分组的背包问题中的一个物品组，每个选择了主件又选择了若干个附件的策略对应于这个物品组中的一个物品，其费用和价值都是这个策略中的物品的值的和。但仅仅是这一步转化并不能给出一个好的算法，因为物品组中的物品还是像原问题的策略一样多。

再考虑分组的背包问题中的一句话：可以对每组中的物品应用完全背包中“一个简单有效的优化”。这提示我们，对于一个物品组中的物品，所有费用相同的物品只留一个价值最大的，不影响结果。所以，我们可以对主件 ![[公式]](https://www.zhihu.com/equation?tex=i) 的“附件集合”先进行一次01背包，得到费用依次为 ![[公式]](https://www.zhihu.com/equation?tex=0..V-c%5Bi%5D) 所有这些值时相应的最大价值 ![[公式]](https://www.zhihu.com/equation?tex=f%27%5B0..V-c%5Bi%5D%5D) 。那么这个主件及它的附件集合相当于 ![[公式]](https://www.zhihu.com/equation?tex=V-c%5Bi%5D%2B1) 个物品的物品组，其中费用为 ![[公式]](https://www.zhihu.com/equation?tex=c%5Bi%5D%2Bk) 的物品的价值为 ![[公式]](https://www.zhihu.com/equation?tex=f%27%5Bk%5D%2Bw%5Bi%5D) 。也就是说原来指数级的策略中有很多策略都是冗余的，通过一次01背包后，将主件 ![[公式]](https://www.zhihu.com/equation?tex=i) 转化为 ![[公式]](https://www.zhihu.com/equation?tex=V-c%5Bi%5D%2B1) 个物品的物品组，就可以直接应用分组的背包问题的算法解决问题了。

更一般的问题

更一般的问题是：依赖关系以图论中“森林”的形式给出（森林即多叉树的集合），也就是说，主件的附件仍然可以具有自己的附件集合，限制只是每个物品最多只依赖于一个物品（只有一个主件）且不出现循环依赖。

解决这个问题仍然可以用将每个主件及其附件集合转化为物品组的方式。唯一不同的是，由于附件可能还有附件，就不能将每个附件都看作一个一般的01背包中的物品了。若这个附件也有附件集合，则它必定要被先转化为物品组，然后用分组的背包问题解出主件及其附件集合所对应的附件组中各个费用的附件所对应的价值。

事实上，这是一种树形DP，其特点是每个父节点都需要对它的各个儿子的属性进行一次DP以求得自己的相关属性。这已经触及到了“泛化物品”的思想。看完下节泛化物品后，你会发现这个“依赖关系树”每一个子树都等价于一件泛化物品，求某节点为根的子树对应的泛化物品相当于求其所有儿子的对应的泛化物品之和。

### 7.3 小结

NOIP2006的那道背包问题我做得很失败，写了上百行的代码，却一分未得。后来我通过思考发现通过引入“物品组”和“依赖”的概念可以加深对这题的理解，还可以解决它的推广问题。用物品组的思想考虑那题中极其特殊的依赖关系：物品不能既作主件又作附件，每个主件最多有两个附件，可以发现一个主件和它的两个附件等价于一个由四个物品组成的物品组，这便揭示了问题的某种本质。

我想说：失败不是什么丢人的事情，从失败中全无收获才是。

## 8. 泛化物品

### 8.1 定义

考虑这样一种物品，它并没有固定的费用和价值，而是它的价值随着你分配给它的费用而变化。这就是泛化物品的概念。

更严格的定义之。在背包容量为 ![[公式]](https://www.zhihu.com/equation?tex=V) 的背包问题中，泛化物品是一个定义域为 ![[公式]](https://www.zhihu.com/equation?tex=0..V) 中的整数的函数 ![[公式]](https://www.zhihu.com/equation?tex=h) ，当分配给它的费用为 ![[公式]](https://www.zhihu.com/equation?tex=v) 时，能得到的价值就是 ![[公式]](https://www.zhihu.com/equation?tex=h%28v%29) 。

这个定义有一点点抽象，另一种理解是一个泛化物品就是一个数组 ![[公式]](https://www.zhihu.com/equation?tex=h%5B0..V%5D) ，给它费用 ![[公式]](https://www.zhihu.com/equation?tex=v) ，可得到价值 ![[公式]](https://www.zhihu.com/equation?tex=h%5BV%5D) 。

一个费用为 ![[公式]](https://www.zhihu.com/equation?tex=c) 价值为 ![[公式]](https://www.zhihu.com/equation?tex=w) 的物品，如果它是01背包中的物品，那么把它看成泛化物品，它就是除了 ![[公式]](https://www.zhihu.com/equation?tex=h%28c%29%3Dw) 其它函数值都为 ![[公式]](https://www.zhihu.com/equation?tex=0) 的一个函数。如果它是完全背包中的物品，那么它可以看成这样一个函数，仅当 ![[公式]](https://www.zhihu.com/equation?tex=v) 被 ![[公式]](https://www.zhihu.com/equation?tex=c) 整除时有 ![[公式]](https://www.zhihu.com/equation?tex=h%28v%29%3Dv%2Fc%2Aw) ，其它函数值均为 ![[公式]](https://www.zhihu.com/equation?tex=0) 。如果它是多重背包中重复次数最多为 ![[公式]](https://www.zhihu.com/equation?tex=n) 的物品，那么它对应的泛化物品的函数有 ![[公式]](https://www.zhihu.com/equation?tex=h%28v%29%3Dv%2Fc%2Aw) 仅当 ![[公式]](https://www.zhihu.com/equation?tex=v) 被 ![[公式]](https://www.zhihu.com/equation?tex=c) 整除且 ![[公式]](https://www.zhihu.com/equation?tex=v%2Fc%3C%3Dn) ，其它情况函数值均为 ![[公式]](https://www.zhihu.com/equation?tex=0) 。

一个物品组可以看作一个泛化物品 ![[公式]](https://www.zhihu.com/equation?tex=h) 。对于一个 ![[公式]](https://www.zhihu.com/equation?tex=0..V) 中的 ![[公式]](https://www.zhihu.com/equation?tex=v) ，若物品组中不存在费用为 ![[公式]](https://www.zhihu.com/equation?tex=v) 的的物品，则 ![[公式]](https://www.zhihu.com/equation?tex=h%28v%29%3D0) ，否则 ![[公式]](https://www.zhihu.com/equation?tex=h%28v%29) 为所有费用为 ![[公式]](https://www.zhihu.com/equation?tex=v) 的物品的最大价值。上节中每个主件及其附件集合等价于一个物品组，自然也可看作一个泛化物品。

泛化物品的和

如果面对两个泛化物品 ![[公式]](https://www.zhihu.com/equation?tex=h) 和 ![[公式]](https://www.zhihu.com/equation?tex=l) ，要用给定的费用从这两个泛化物品中得到最大的价值，怎么求呢？事实上，对于一个给定的费用 ![[公式]](https://www.zhihu.com/equation?tex=v) ，只需枚举将这个费用如何分配给两个泛化物品就可以了。同样的，对于 ![[公式]](https://www.zhihu.com/equation?tex=0..V) 的每一个整数 ![[公式]](https://www.zhihu.com/equation?tex=v) ，可以求得费用 ![[公式]](https://www.zhihu.com/equation?tex=v) 分配到 ![[公式]](https://www.zhihu.com/equation?tex=h) 和 ![[公式]](https://www.zhihu.com/equation?tex=l) 中的最大价值 ![[公式]](https://www.zhihu.com/equation?tex=f%28v%29) 。也即 ![[公式]](https://www.zhihu.com/equation?tex=f%28v%29%3D%5Cmax%5C%7Bh%28k%29+%2Bl%28v-k%29~%7C~0%3C%3Dk%3C%3Dv%5C%7D) 。可以看到， ![[公式]](https://www.zhihu.com/equation?tex=f) 也是一个由泛化物品 ![[公式]](https://www.zhihu.com/equation?tex=h) 和 ![[公式]](https://www.zhihu.com/equation?tex=l) 决定的定义域为 ![[公式]](https://www.zhihu.com/equation?tex=0..V) 的函数，也就是说， ![[公式]](https://www.zhihu.com/equation?tex=f) 是一个由泛化物品 ![[公式]](https://www.zhihu.com/equation?tex=h) 和 ![[公式]](https://www.zhihu.com/equation?tex=l) 决定的泛化物品。

由此可以定义泛化物品的和： ![[公式]](https://www.zhihu.com/equation?tex=h) 、 ![[公式]](https://www.zhihu.com/equation?tex=l) 都是泛化物品，若泛化物品 ![[公式]](https://www.zhihu.com/equation?tex=f) 满足 ![[公式]](https://www.zhihu.com/equation?tex=f%28v%29%3D%5Cmax%5C%7Bh%28k%29%2Bl%28v-k%29~%7C~0%3C%3Dk%3C%3Dv%5C%7D) ，则称f是 ![[公式]](https://www.zhihu.com/equation?tex=h) 与 ![[公式]](https://www.zhihu.com/equation?tex=l) 的和，即 ![[公式]](https://www.zhihu.com/equation?tex=f%3Dh%2Bl) 。这个运算的时间复杂度是 ![[公式]](https://www.zhihu.com/equation?tex=O%28V%5E2%29) 。

泛化物品的定义表明：在一个背包问题中，若将两个泛化物品代以它们的和，不影响问题的答案。事实上，对于其中的物品都是泛化物品的背包问题，求它的答案的过程也就是求所有这些泛化物品之和的过程。设此和为s，则答案就是s[0..V]中的最大值。

背包问题的泛化物品

一个背包问题中，可能会给出很多条件，包括每种物品的费用、价值等属性，物品之间的分组、依赖等关系等。但肯定能将问题对应于某个泛化物品。也就是说，给定了所有条件以后，就可以对每个非负整数v求得：若背包容量为 ![[公式]](https://www.zhihu.com/equation?tex=v) ，将物品装入背包可得到的最大价值是多少，这可以认为是定义在非负整数集上的一件泛化物品。这个泛化物品——或者说问题所对应的一个定义域为非负整数的函数——包含了关于问题本身的高度浓缩的信息。一般而言，求得这个泛化物品的一个子域（例如 ![[公式]](https://www.zhihu.com/equation?tex=0..V) ）的值之后，就可以根据这个函数的取值得到背包问题的最终答案。

综上所述，一般而言，求解背包问题，即求解这个问题所对应的一个函数，即该问题的泛化物品。而求解某个泛化物品的一种方法就是将它表示为若干泛化物品的和然后求之。

### 8.2 小结

本讲可以说都是我自己的原创思想。具体来说，是我在学习函数式编程的Scheme语言时，用函数编程的眼光审视各类背包问题得出的理论。这一讲真的很抽象，也许在“模型的抽象程度”这一方面已经超出了NOIP的要求，所以暂且看不懂也没关系。相信随着你的OI之路逐渐延伸，有一天你会理解的。

我想说：“思考”是一个OIer最重要的品质。简单的问题，深入思考以后，也能发现更多。

\9. 背包问题问法的变化

以上涉及的各种背包问题都是要求在背包容量（费用）的限制下求可以取到的最大价值，但背包问题还有很多种灵活的问法，在这里值得提一下。但是我认为，只要深入理解了求背包问题最大价值的方法，即使问法变化了，也是不难想出算法的。

例如，求解最多可以放多少件物品或者最多可以装满多少背包的空间。这都可以根据具体问题利用前面的方程求出所有状态的值（f数组）之后得到。

还有，如果要求的是“总价值最小”“总件数最小”，只需简单的将上面的状态转移方程中的 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmax) 改成 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmin) 即可。

下面说一些变化更大的问法。

输出方案

一般而言，背包问题是要求一个最优值，如果要求输出这个最优值的方案，可以参照一般动态规划问题输出方案的方法：记录下每个状态的最优值是由状态转移方程的哪一项推出来的，换句话说，记录下它是由哪一个策略推出来的。便可根据这条策略找到上一个状态，从上一个状态接着向前推即可。

还是以01背包为例，方程为 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%5Cmax%5C%7Bf%5Bi-1%5D%5Bv%5D~%2C~f%5Bi-1%5D%5Bv-c%5Bi%5D%5D%2Bw%5Bi%5D%5C%7D) 。再用一个数组 ![[公式]](https://www.zhihu.com/equation?tex=g%5Bi%5D+%5Bv%5D) ，设 ![[公式]](https://www.zhihu.com/equation?tex=g%5Bi%5D%5Bv%5D%3D0) 表示推出 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 的值时是采用了方程的前一项（也即 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3Df%5Bi-1%5D%5Bv%5D) ）， ![[公式]](https://www.zhihu.com/equation?tex=g%5Bi%5D%5Bv%5D) 表示采用了方程的后一项。注意这两项分别表示了两种策略：未选第 ![[公式]](https://www.zhihu.com/equation?tex=i) 个物品及选了第 ![[公式]](https://www.zhihu.com/equation?tex=i) 个物品。那么输出方案的伪代码可以这样写（设最终状态为 ![[公式]](https://www.zhihu.com/equation?tex=f%5BN%5D%5BV%5D) ）：

```cpp
i=N
v=V
while(i>0)
    if(g[i][v]==0)
        print "未选第i项物品"
    else if(g[i][v]==1)
        print "选了第i项物品"
        v=v-c[i]
```

另外，采用方程的前一项或后一项也可以在输出方案的过程中根据 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 的值实时地求出来，也即不须纪录 ![[公式]](https://www.zhihu.com/equation?tex=g) 数组，将上述代码中的 ![[公式]](https://www.zhihu.com/equation?tex=g%5Bi%5D+%5Bv%5D%3D%3D0) 改成 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%3Df%5Bi-1%5D%5Bv%5D) ， ![[公式]](https://www.zhihu.com/equation?tex=g%5Bi%5D%5Bv%5D%3D%3D1) 改成 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%3Df%5Bi-1%5D%5Bv-c%5Bi%5D%5D%2Bw%5Bi%5D) 也可。

输出字典序最小的最优方案

这里“字典序最小”的意思是 ![[公式]](https://www.zhihu.com/equation?tex=1..N) 号物品的选择方案排列出来以后字典序最小。以输出01背包最小字典序的方案为例。

一般而言，求一个字典序最小的最优方案，只需要在转移时注意策略。首先，子问题的定义要略改一些。我们注意到，如果存在一个选了物品1的最优方案，那么答案一定包含物品 ![[公式]](https://www.zhihu.com/equation?tex=1) ，原问题转化为一个背包容量为 ![[公式]](https://www.zhihu.com/equation?tex=v-c%5B1%5D) ，物品为 ![[公式]](https://www.zhihu.com/equation?tex=2..N) 的子问题。反之，如果答案不包含物品 ![[公式]](https://www.zhihu.com/equation?tex=1) ，则转化成背包容量仍为 ![[公式]](https://www.zhihu.com/equation?tex=V) ，物品为 ![[公式]](https://www.zhihu.com/equation?tex=2..N) 的子问题。不管答案怎样，子问题的物品都是以 ![[公式]](https://www.zhihu.com/equation?tex=i..N) 而非前所述的 ![[公式]](https://www.zhihu.com/equation?tex=1..i) 的形式来定义的，所以状态的定义和转移方程都需要改一下。但也许更简易的方法是先把物品逆序排列一下，以下按物品已被逆序排列来叙述。

在这种情况下，可以按照前面经典的状态转移方程来求值，只是输出方案的时候要注意：从 ![[公式]](https://www.zhihu.com/equation?tex=N) 到 ![[公式]](https://www.zhihu.com/equation?tex=1) 输入时，如果 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%3Df%5Bi-v%5D) 及 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%3Df%5Bi-1%5D%5Bf-c%5Bi%5D%5D%2Bw%5Bi%5D) 同时成立，应该按照后者（即选择了物品 ![[公式]](https://www.zhihu.com/equation?tex=i) ）来输出方案。

求方案总数

对于一个给定了背包容量、物品费用、物品间相互关系（分组、依赖等）的背包问题，除了再给定每个物品的价值后求可得到的最大价值外，还可以得到装满背包或将背包装至某一指定容量的方案总数。

对于这类改变问法的问题，一般只需将状态转移方程中的 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmax) 改成 ![[公式]](https://www.zhihu.com/equation?tex=sum) 即可。例如若每件物品均是01背包中的物品，转移方程即为 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D%3D%5Csum%5C%7Bf%5Bi-1%5D%5Bv%5D~%2C~f%5Bi-1%5D%5Bv-c%5Bi%5D%5D%2Bw%5Bi%5D%5C%7D) ，初始条件 ![[公式]](https://www.zhihu.com/equation?tex=f%5B0%5D%5B0%5D%3D1) 。

事实上，这样做可行的原因在于状态转移方程已经考察了所有可能的背包组成方案。

最优方案的总数

这里的最优方案是指物品总价值最大的方案。还是以01背包为例。

结合求最大总价值和方案总数两个问题的思路，最优方案的总数可以这样求： ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 意义同前述， ![[公式]](https://www.zhihu.com/equation?tex=g%5Bi%5D%5Bv%5D) 表示这个子问题的最优方案的总数，则在求 ![[公式]](https://www.zhihu.com/equation?tex=f%5Bi%5D%5Bv%5D) 的同时求 ![[公式]](https://www.zhihu.com/equation?tex=g%5Bi%5D%5Bv%5D) 的伪代码如下：

```cpp
for i=1..N
   for v=0..V
       f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}
       g[i][v]=0
       if(f[i][v]==f[i-1][v])
           inc(g[i][v],g[i-1][v]
       if(f[i][v]==f[i-1][v-c[i]]+w[i])
           inc(g[i][v],g[i-1][v-c[i]])
```

如果你是第一次看到这样的问题，请仔细体会上面的伪代码。

小结

显然，这里不可能穷尽背包类动态规划问题所有的问法。甚至还存在一类将背包类动态规划问题与其它领域（例如数论、图论）结合起来的问题，在这篇论背包问题的专文中也不会论及。但只要深刻领会前述所有类别的背包问题的思路和状态转移方程，遇到其它的变形问法，只要题目难度还属于NOIP，应该也不难想出算法。

触类旁通、举一反三，应该也是一个OIer应有的品质吧。