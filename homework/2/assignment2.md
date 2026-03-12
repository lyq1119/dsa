# Assignment #2: 位运算、前缀和、树状数组、归并排序 & 状态压缩
兰玉琪 2500010774 数学科学学院

## 1. 题目

### E868.二进制间距

bit manipulation, https://leetcode.cn/problems/binary-gap/

> 主要是练习面向对象编程写法，这样力扣题目，笔试都没有问题了。机考时候，不是必须OOP，能AC就可以。
>

思路：



代码：

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        gap = 0
        begin = s.index("1")
        end = begin
        while end < len(s):
            if begin == end:
                end += 1
            elif s[end] != "1":
                end += 1
            elif s[end] == "1":
                gap = max(gap,end-begin)
                begin = end
        return gap
```

![alt text](截屏2026-03-11%2013.04.43.png)

### M304.二维区域和检索 - 矩阵不可变

prefix sum, https://leetcode.cn/problems/range-sum-query-2d-immutable/


思路：



代码：

```python
class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        n = len(matrix)
        m = len(matrix[0])
        self.dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                self.dp[i][j] = self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]+self.matrix[i-1][j-1]
        print(self.dp)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        return self.dp[row2][col2]-self.dp[row2][col1-1]-self.dp[row1-1][col2]+self.dp[row1-1][col1-1]
```


![alt text](截屏2026-03-11%2013.28.47.png)



### M1680.连接连续二进制数字

bit manipulation, https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/



思路：



代码：

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        zhi = 0
        ermi = 1
        for t in range(n,0,-1):
            zhi += ermi*t
            zhi %= (10**9+7)
            ermi *= ((2**(len(bin(t))-2))%(10**9+7))
            ermi %= (10**9+7)
        return zhi
```


![alt text](截屏2026-03-11%2013.30.46.png)


### M1461.检查一个字符串是否包含所有长度为 K 的二进制子串

bit manipulation, https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/



思路：



代码：

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool: 
        if len(s) < k:
            return False
        storage = set()
        curstr = [s[j] for j in range(k-1)]
        for i in range(len(s)-k+1):
            curstr.append(s[i+k-1])
            storage.add("".join(curstr))
            curstr.pop(0)
        if len(storage) == (1<<k):
            return True
        return False
```

![alt text](截屏2026-03-11%2013.35.04.png)





### M30178:数字华容道（Easy Version）

merge sort, binary indexed tree, http://cs101.openjudge.cn/practice/30178/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T30201: 旅行售货商问题

bitmask dp, http://cs101.openjudge.cn/practice/30201/

思路：



代码：

```python
from collections import deque
n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))
k = (1<<n)
matrix = [[float("inf") for _ in range(n)] for __ in range(k)]
matrix[1][0] = 0
minimum = float("inf")
for visit in range(2,k):
    for cur in range(1,n):
        if visit & 1 == 0:
            continue
        if (1<<cur)|visit != visit:
            continue
        visitnew = visit - (1<<cur)
        for i in range(n):
            if (1<<i)|visitnew != visitnew:
                continue
            a = matrix[visitnew][i]+cost[cur][i]
            if a >= matrix[visit][cur]:
                continue
            matrix[visit][cur] = a
for i in range(1,n):
    minimum = min(minimum,cost[i][0]+matrix[k-1][i])
print(minimum)
```



![alt text](截屏2026-03-11%2014.33.25.png)





## 2. 学习总结和个人收获
月考1小时ak，还是很轻松的，说明上学期学的东西还挺扎实，必须得感谢闫老师给我打下的基础
