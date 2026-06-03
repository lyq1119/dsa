# DSA Assignment #B: 20260513 模拟考
2500010774 兰玉琪 数学科学学院
## 1. 题目
### E02724: 生日相同
sortings, http://cs101.openjudge.cn/pctbook/E02724/
思路：
代码：
```python
n = int(input())
birthday = {}
for _ in range(n):
    xuehao,yue,ri = input().split()
    yue = int(yue)
    ri = int(ri)
    if (yue,ri) not in birthday:
        birthday[(yue,ri)] = []
    birthday[(yue,ri)].append(xuehao)
keys = [key for key in birthday]
keys.sort()
for riqi in keys:
    xuehaoji = birthday[riqi]
    newlist = [riqi[0],riqi[1]]+xuehaoji
    if len(xuehaoji) > 1:
        print(*newlist)
```
![alt text](截屏2026-05-14%2001.11.11.png)
### E19963: 买学区房
math, http://cs101.openjudge.cn/practice/19963
思路：
代码：
```python
n = int(input())
dist = []
mylist = input().split()
pairs = [i[1:-1] for i in mylist]
dist = [sum(map(int,i.split(','))) for i in pairs]
cost = list(map(int,input().split()))
xingjiabi = sorted([(dist[i]/cost[i],i) for i in range(n)])
available = [True for _ in range(n)]
cost = [(cost[i],i) for i in range(n)]
cost.sort()
if n % 2 == 0:
    xz = (xingjiabi[n//2-1][0]+xingjiabi[n//2][0])/2
    cz = (cost[n//2-1][0]+cost[n//2][0])/2
else:
    xz = xingjiabi[n//2][0]
    cz = cost[n//2][0]
for a,b in xingjiabi:
    if a <= xz:
        available[b] = False   
for a,b in cost:
        if a >= cz:
            available[b] = False 
print(available.count(True))
```
![alt text](截屏2026-05-14%2001.12.29.png)
### M20746: 满足合法工时的最少人数
binary search, http://cs101.openjudge.cn/practice/20746/
思路：
代码：
```python
mylist = list(map(int,input().split(",")))
t = int(input())
left,right = 1,max(mylist)
def check(i):
    total = 0
    for j in range(len(mylist)):
        total += (mylist[j]-1)//i + 1
    if total <= t:
        return True
    return False
while left < right:
    mid = (left+right)//2
    if check(mid):
        right = mid
    else:
        left = mid+1
print(left)
```
![alt text](截屏2026-05-14%2001.13.03.png)
### M07734: 虫子的生活
DSU, http://cs101.openjudge.cn/practice/07734/
思路：
代码：
```python
n = int(input())
def solve():
    m,t = map(int,input().split())
    Parent = [i for i in range(m)]
    type = [0 for __ in range(m)]
    def find(i):
        if (Parent[i] == i):
            return i
        else:
            result = find(Parent[i])
            type[i] = (type[Parent[i]] + type[i])%2
            Parent[i] = result
            return result
    def union(i,j):
        x1 = find(i)
        y1 = find(j)
        if x1 == y1:
            return type[i] != type[j]
        Parent[y1] = x1
        type[y1] = (1+type[i]+type[j])%2
        return True
    verdict = True
    for _ in range(t):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        verdict = verdict and union(a,b)
    if verdict:
        print("No suspicious bugs found!")
    else:
        print("Suspicious bugs found!")
    return
for _ in range(n):
    print(f"Scenario #{_+1}:")
    solve()
    if _ != n-1:
        print("")
```
![alt text](截屏2026-05-14%2001.13.49.png)
### M02186: Popular Cows
SCC, http://cs101.openjudge.cn/practice/02186/
思路：
代码
```python
n,m = map(int,input().split())
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
adj = defaultdict(list)
for _ in range(m):
    i,j = map(int,input().split())
    i -= 1
    j -= 1
    adj[i].append(j)
visited = [False] * n
stack = []
def dfs1(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs1(v)
    stack.append(u) 
for i in range(n):
    if not visited[i]:
        dfs1(i)
# 2. 创建反向图
rev_adj = [[] for _ in range(n)]
for u in range(n):
    for v in adj[u]:
        rev_adj[v].append(u)
# 3. 反向 DFS，提取 SCC
visited = [False] * n
index = 0
scc = [0 for _ in range(n)]
count = [0 for _ in range(n)]
def dfs2(u,index):
    scc[u] = index
    count[index] += 1
    visited[u] = True
    for v in rev_adj[u]:
        if not visited[v]:
            dfs2(v,index)
while stack:
    u = stack.pop()
    if not visited[u]:
        dfs2(u,index)
        index += 1
chudu = [0 for _ in range(index)]
for i in range(n):
    for j in adj[i]:
        if scc[i] == scc[j]:
            continue
        else:
            chudu[scc[i]] += 1
total = 0
visit = 0
for i in range(index):
    if chudu[i] == 0:
        visit += 1
        total = count[i]
if visit == 1:
    print(total)
else:
    print(0)
```
![alt text](截屏2026-05-14%2001.15.32.png)
### T01236: Network of Schools 238
SCC, http://cs101.openjudge.cn/practice/01236/
思路：
代码
```python
n = int(input())
from collections import defaultdict
adj = {}
for i in range(n):
    mylist = list(map(int,input().split()))[:-1]
    adj[i] = [mylist[i]-1 for i in range(len(mylist))]
# 1. 正向 DFS，记录完成顺序
visited = [False] * n
stack = []
def dfs1(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs1(v)
    stack.append(u)  # 回溯时压入栈
for i in range(n):
    if not visited[i]:
        dfs1(i)
# 2. 创建反向图
rev_adj = [[] for _ in range(n)]
for u in range(n):
    for v in adj[u]:
        rev_adj[v].append(u)
# 3. 反向 DFS，提取 SCC
visited = [False] * n
sccs = []
def dfs2(u, current_scc):
    visited[u] = True
    current_scc.append(u)
    for v in rev_adj[u]:
        if not visited[v]:
            dfs2(v, current_scc)
while stack:
    u = stack.pop()
    if not visited[u]:
        current_scc = []
        dfs2(u, current_scc)
        sccs.append(current_scc)
# 给每个点分配SCC编号
scc_id = [0] * n
for i in range(len(sccs)):
    for node in sccs[i]:
        scc_id[node] = i
# 构建缩点后的 DAG & 计算出度
dag = [[] for _ in range(len(sccs))]
in_degree = [0] * len(sccs)
out_degree = [0] * len(sccs)
edges = set()  # 防止重复建边
for u in range(n):
    for v in adj[u]:
        a = scc_id[u]
        b = scc_id[v]
        if a != b and (a, b) not in edges:
            edges.add((a, b))
            dag[a].append(b)
            in_degree[b] += 1
            out_degree[a] += 1
print(in_degree.count(0))
if len(sccs) == 1:
    print(0)
else:
    print(max(in_degree.count(0),out_degree.count(0)))
```
![alt text](截屏2026-05-14%2001.16.17.png)

## 2. 学习总结和个人收获
非常感谢闫老师的模拟考，对我平静的生活起到了极大的震荡，让我彻底摆脱以前的懒散与浮躁，潜下心来学知识
这次发挥的很不好，只ac了4，SCC可谓是不会一点，以前假期学的忘光光，而且状态也不是很好
真的要被自己笑死，第一个题一上来就被wa，还好我是老将，并没有太放心上
然后再做第二个题，又wa，后面检查发现原来是没有看到是严格大于小于，这种低级失误我还犯，可见当时脑子不知道在干什么
我发现我的心态真的无敌好，我并没有因此而心态炸掉
我接着做3，然后我想了想，发现思路几乎都是超时的，然后就去看4去了，4很轻松拿下，别笑这是我第一道ac的题
然后5也很轻松拿下
然后2检查出错误，然后拿下
然后3写了一个思路交了，发现runtime error
然后又回去看1，然后发现我的弱智错误，竟然忘了只有一个人的日期不用输出，然后拿下
然后3和6就都不会，左右脑互搏，然后在最后15分钟想到SCC了，但是又不敢写，这里严肃谴责一下我自己，没有上学期勇敢
反正我发现我考试的心态一直倒是很平稳，反倒是考后难过了很久，哎，不能再摆了，即使假期学了也得复健啊
考完试的晚上苯j人已经列好所有的知识点和期末复习计划，感觉心里踏实了不少，也开始想起来上学期复习的小窍门
现在在一直完善我的cheatsheet