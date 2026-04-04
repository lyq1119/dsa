# DSA Assignment #5: 20260401 cs201 Mock Exam
2500010774 兰玉琪 数学科学学院
## 1. 题目

### E02039: 反反复复	

matrix, http://cs101.openjudge.cn/practice/02039/

思路：



代码：

```python
n = int(input())
string = input()
mystr = ""

for j in range(n):
    for i in range(len(string)//n):
        if i % 2 == 0:
            mystr += string[n*i+j]
        else:
            mystr += string[n*i+n-j-1]

print(mystr)
```


![alt text](截屏2026-04-04%2008.56.21.png)


### E02092: Grandpa is Famous	

implementation, http://cs101.openjudge.cn/practice/02092/


思路：



代码：

```python
import sys
from collections import defaultdict
data = list(map(int,sys.stdin.read().split()))
i = 0
while True:
    if data[i] == 0 and data[i+1] == 0:
        break
    N,M = data[i],data[i+1]
    i += 2
    mydict = defaultdict(int)
    for _ in range(N*M):
        mydict[data[i]] += 1
        i += 1
    mylist = sorted(mydict,key=lambda x:mydict[x],reverse=True)
    val = mydict[mylist[1]]
    result= []
    for j in range(1,len(mylist)):
        if mydict[mylist[j]] != val:
            break
        result.append(mylist[j])
    print(*list(sorted(result)))
```
![alt text](截屏2026-04-04%2008.57.07.png)

### M02774: 木材加工	

binary search, http://cs101.openjudge.cn/practice/02774/

思路：



代码：

```python
N,K = map(int,input().split())
woods = []
def testavail(t,woods):
    total = 0
    for wood in woods:
        total += wood//t
    return total
for _ in range(N):
    woods.append(int(input()))
if sum(woods) < K:
    print(0)
else:
    left,right = 1,max(woods)
    if left == right:
        print(1)
    while left < right:
        mid = (left+right)//2
        if testavail(mid,woods) < K:
            right = mid-1
        else:
            left = mid
        if left == right:
            print(left)
            break
        if right - left == 1:
            if testavail(right,woods) < K:
                print(left)
            else:
                print(right)
            break
```
![alt text](截屏2026-04-04%2008.58.27.png)

### M04077: 出栈序列统计

dp, dfs, math, http://cs101.openjudge.cn/practice/04077/

思路：



代码：

```python
count = 0
n = int(input())
possible = set()
def fun(i,stack,result):
    if len(result) == n:
        possible.add(tuple(result.copy()))
        return
    if stack:
        s = stack[-1]
        fun(i,stack[:-1],result+[s])
    if i <= n-1:
        fun(i+1,stack+[i+1],result)
fun(0,[],[])
print(len(possible))
```
![alt text](截屏2026-04-04%2008.59.16.png)

### M30637: 合法出栈序列pub

stack, http://cs101.openjudge.cn/practice/M30637/

思路：



代码

```python
mystr = input()
n = len(mystr)
while True:
    try:
        string = input()
        if len(string) != n:
            print("NO")
            continue
        stack = []
        def fun(i,j):
            if i == n:
                if j == n:
                    return True
                t = stack.pop()
                if t != string[j]:
                    return False
                return fun(i,j+1)
            if mystr[i] == string[j]:
                return fun(i+1,j+1)
            if string[j] in stack:
                if stack.pop() != string[j]:
                    return False
                return fun(i,j+1)
            stack.append(mystr[i])
            return fun(i+1,j)
        if fun(0,0):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
```

![alt text](截屏2026-04-04%2008.59.57.png)


### T30102:完美交易窗口

monotonic stack, http://cs101.openjudge.cn/practice/T30102/

思路：
考场上一紧张题读错了，然后思路也有漏洞，妄想一次单调栈就结束问题
然后课后怒干1.5h用pypy成功ac
[3,1,2,5,4,6,1,2,4,3,5]
我的思路是扫两遍单调栈
mylist1存每个位置能向右延伸的最大的坐标 [0, 5, 5, 3, 5, 5, 9, 9, 8, 9]
mylist2存每个位置能向左延伸的最小的坐标 [0, 1, 1, 0, 4, 0, 6, 6, 6, 9]
然后我希望对(i,mylist1[i])找(mylist2[j],j)使得i>=mylist2[j]且mylist1[i]>=j>=i
countlist[t]存mylist2中等于t的下标 [[0, 3, 5], [1, 2], [], [], [4], [], [6, 7, 8], [], [], [9]]
在0到mylist1[i]找最大的在countlist[0]或countlist[1]或……或countlist[i]中的数
记countlist[0]和countlist[1]和……和countlist[i]中的数构成集合S
用树状数组，维护S(i)为S中<=i的数的个数
如果S(mylist1[i])是0说明我们要找的j不存在
如果不是0说明我们的j存在，然后去找值为S(mylist1[i])-1的S(k)且S(k+1)=S(mylist1[i])
这样我们要找的j就是k+1
然后去更新maxlength就好，注意maxlength不能是1，所以得不允许k+1是i的情况
代码

```python
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def lowbit(self, x):
        return x & -x
    def update(self, i, delta):
        """将第 i 个元素增加 delta"""
        while i <= self.size:
            self.tree[i] += delta
            i += self.lowbit(i)
    def query(self, i):
        """查询前 i 个元素的和"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= self.lowbit(i)
        return s
    
n = int(input())
stocks = []
for _ in range(n):
    stocks.append(int(input()))
mylist1 = [n-1 for _ in range(n)]
stack = []
for i in range(n):
    while stack and stocks[i] <= stocks[stack[-1]]:
        mylist1[stack.pop()] = i-1
    stack.append(i)
stack = []
mylist2 = [0 for _ in range(n)]
countlist = [[] for _ in range(n)]
for i in range(n-1,-1, -1):
    while stack and stocks[i] >= stocks[stack[-1]]:
        t= stack.pop()
        mylist2[t] = i+1
        countlist[i+1].append(t)
    stack.append(i)
for i in range(n):
    if mylist2[i] == 0:
        countlist[0].append(i)
tree = BIT(n)
maxlength = 0
for i in range(n):
    for t in countlist[i]:
        tree.update(t+1, 1)
    a = tree.query(mylist1[i]+1)
    if a == 0:
        continue
    left,right = i+1,mylist1[i]+1
    if left == right:
        continue
    while left < right:
        mid = (left + right) // 2
        if tree.query(mid) == a:
            right = mid
        else:
            left = mid
        if left == right - 1:
            if tree.query(right) == a:
                maxlength = max(maxlength, right-i)
            else:
                maxlength = max(maxlength, right-i+1)
            break
print(maxlength)
```

![alt text](截屏2026-04-04%2008.43.34.png)

## 2. 学习总结和个人收获
求求闫老师在课上讲一讲月考最后一道题，爬群 is overwhelming
最近有点忙，感觉开学到现在一直在吃老本（hhh其实老本确实很够吃，就是熟练度的问题
最近就只跟着做每日选做了，老师讲义里的题我都做过了www