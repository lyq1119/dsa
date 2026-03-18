# Assignment #3: 20260311 cs201 Mock Exam
2500010774 兰玉琪 数学科学学院
## 1. 题目
### E20742:泰波拿契數

implementation, http://cs101.openjudge.cn/practice/20742/

思路：



代码：

```python
n = int(input())
def dfs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return dfs(n-1)+dfs(n-2)+dfs(n-3)
print(dfs(n))
```



![alt text](截屏2026-03-11%2013.04.43.png)





### E30571.十进制整数的反码

bit manipulation, http://cs101.openjudge.cn/practice/E30571/



思路：



代码：

```python
import math
n = int(input())
t = int(math.log2(n))+1
print((1<<t)-1-n)
```

![alt text](截屏2026-03-15%2018.00.31.png)

### E29950:稳定的符文序列

two pointers, http://cs101.openjudge.cn/practice/E29950

思路：

代码：
```python
begin = 0
end = 0
s = input()
n = len(s)
myset = set()
for i in range(n):
    if s[i] in myset:
        break
    myset.add(s[i])
    end = i
maxlength = end + 1
while True:
    end += 1
    if end == n:
        break
    if s[end] not in myset:
        myset.add(s[end])
        maxlength = max(maxlength,end-begin+1)
        continue
    while s[begin] != s[end]:
        myset.discard(s[begin])
        begin += 1   
    begin += 1
    maxlength = max(maxlength,end-begin+1)
print(maxlength)
```
![alt text](截屏2026-03-15%2018.10.06.png)

### M30218:狭路相逢

stack, http://cs101.openjudge.cn/practice/M30218/


思路：



代码：

```python
n = int(input())
mylist = list(map(int,input().split()))
result = []
for num in mylist:
    if not result:
        result.append(num)
    else:
        flag = True
        while result:
            a = result[-1]
            if num < 0:
                if a < 0:
                    result.append(num)
                    flag = False
                    break
                else:
                    if a > -num:
                        result.pop()
                        result.append(a+num)
                        flag = False
                        break
                    else:
                        result.pop()
                        num += a
            elif num > 0:
                result.append(num)
                flag = False
                break
            elif num == 0:
                flag = False
                break
        if flag:
            result.append(num)
print(len(result))
print(*result)
```

![alt text](截屏2026-03-15%2018.08.10.png)



### M02299: Ultra-QuickSort

merge sort, http://cs101.openjudge.cn/practice/02299/

思路：



代码：

```python
def ultrasort(mylist):
    count = 0
    def mergesort(i,j):
        nonlocal count
        if i == j:
            return [mylist[i]]
        med = (i+j)//2
        list1 = mergesort(i,med)
        list2 = mergesort(med+1,j)
        t,s = -1,-1
        list3 = []
        while True:
            if t == len(list1)-1:
                list3.extend(list2[s+1:])
                break
            if s == len(list2)-1:
                list3.extend(list1[t+1:])
                break
            if list1[t+1] < list2[s+1]:
                list3.append(list1[t+1])
                t += 1
            else:
                list3.append(list2[s+1])
                s += 1
                count += len(list1)-t-1
        return list3
    mergesort(0,len(mylist)-1)
    return count
while True:
    n = int(input())
    if n == 0:
        break
    mylist = []
    for _ in range(n):
        mylist.append(int(input()))
    print(ultrasort(mylist))
```

![alt text](截屏2026-03-15%2018.01.25.png)


### M29954:逃离紫罗兰监狱

bfs, http://cs101.openjudge.cn/practice/29954 

思路：



代码：

```python
r,c,k = map(int,input().split())
matrix = []
for _ in range(r):
    mylist = list(input())
    matrix.append(mylist)
    if "S" in mylist:
        a = mylist.index("S")
        sx,sy = _,a
    if "E" in mylist:
        a = mylist.index("E")
        ex,ey = _,a
from collections import deque
def bfs():
    queue = deque([(sx,sy,0,0)])
    visited = {(sx,sy,0)}
    vectors = [(0,1),(1,0),(-1,0),(0,-1)]
    while queue:
        a,b,step,mag = queue.popleft()
        for i,j in vectors:
            if a+i == ex and b+j == ey:
                return step+1
            if a+i >= 0 and a+i <= r-1 and b+j >= 0 and b+j <= c-1:
                if matrix[a+i][b+j] == "." and (a+i,b+j,mag) not in visited:
                    queue.append((a+i,b+j,step+1,mag))
                    visited.add((a+i,b+j,mag))
                if matrix[a+i][b+j] == "#" and (a+i,b+j,mag+1) not in visited and mag < k:
                    queue.append((a+i,b+j,step+1,mag+1))
                    visited.add((a+i,b+j,mag+1))
    return -1
print(bfs()) 
```

![alt text](截屏2026-03-15%2018.02.19.png)



## 2. 学习总结和个人收获
坚持做每日选做





