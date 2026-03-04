# Assignment #1: OOP
兰玉琪 数学科学学院 2500010774

## 1. 题目
### E27653: Fraction类

OOP, http://cs101.openjudge.cn/pctbook/E27653/

> 主要是练习面向对象编程写法，这样力扣题目，笔试都没有问题了。机考时候，不是必须OOP，能AC就可以。
>

思路：



代码：

```python
def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while a and b:
        a,b = b,a%b
    return a
class Fraction:
    def __init__(self,fenzi,fenmu):
        if fenmu < 0:
            fenzi = -fenzi
            fenmu = -fenmu
        self.fenzi = fenzi
        self.fenmu = fenmu
    
    def show(self):
        print(str(self.fenzi)+"/"+str(self.fenmu))
    
    def huajian(self):
        a,b = self.fenzi,self.fenmu
        if a == 0:
            return Fraction(0,1)
        t = gcd(abs(a),abs(b))
        return Fraction(a//t,b//t)

    def __add__(self,Fraction1):
        qitafenzi = Fraction1.fenzi
        qitafenmu = Fraction1.fenmu
        newfenmu = qitafenmu*self.fenmu
        newfenzi = (qitafenzi*self.fenmu)+(self.fenzi*qitafenmu)
        return Fraction(newfenzi,newfenmu).huajian()
a,b,c,d = map(int,input().split())
f1 = Fraction(a,b)
f2 = Fraction(c,d)
f = f1+f2
f.show()
```


![alt text](截屏2026-03-03%2015.24.24.png)





### E190.颠倒二进制位

bit manipulation, https://leetcode.cn/problems/reverse-bits/


思路：



代码：

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        t = bin(n)[2:][::-1]
        s = 32 - len(t)
        m = 0
        for i in range(1,len(t)+1):
            m += int(t[-i])*(2**(i-1))
        return m*(2**s)
```


![alt text](截屏2026-03-03%2015.26.14.png)





### E1356.根据数字二进制下 1 的数目排序

bit manipulation, https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/

思路：



代码：

```python
from collections import defaultdict
class Solution:
    def sortByBits(self, arr):
        arr.sort()
        mylist = []
        mydict = defaultdict(list)
        for num in arr:
            t = bin(num).count("1")
            mydict[t].append(num)
        for s in sorted(list(mydict)):
            mylist.extend(mydict[s])
        return mylist
```


![alt text](截屏2026-03-03%2015.35.24.png)




### M27300: 模型整理

sortings, AI, http://cs101.openjudge.cn/pctbook/M27300/



思路：



代码：

```python
from collections import defaultdict
n = int(input())
mydictM = defaultdict(list)
mydictB = defaultdict(list)
moxinglist = set()
for _ in range(n):
    moxing,canshu = input().split("-")
    moxinglist.add(moxing)
    if canshu[-1] == "B":
        mydictB[moxing].append(canshu)
    else:
        mydictM[moxing].append(canshu)
moxinglist = list(moxinglist)
moxinglist.sort()
for key in moxinglist:
    Mlist = mydictM[key]
    Blist = mydictB[key]
    mytuplesM = [(float(canshu[:-1]),canshu) for canshu in Mlist]
    mytuplesB = [(float(canshu[:-1]),canshu) for canshu in Blist]
    mytuplesM.sort()
    mytuplesB.sort()
    mystring = key+": "
    mystring += ", ".join([yuanzu[1] for yuanzu in mytuplesM])
    if mytuplesM and mytuplesB:
        mystring += ", "
    mystring += ", ".join([yuanzu[1] for yuanzu in mytuplesB])
    print(mystring)
```



![alt text](截屏2026-03-03%2015.37.28.png)





### M1536.排布二进制网格的最少交换次数

greedy, matrix, https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/



思路：



代码：

```python
import math
class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        result = []
        count = 0
        for row in grid:
            t = "".join([str(num) for num in row])
            s = int(t,2)
            if s:
                result.append(int(math.log2(s&(-s))))
            else:
                result.append(n)
        for i in range(n):
            if result[i] < n-i-1:
                flag = False
                for j in range(i+1,n):
                    if result[j] >= n-i-1:
                        flag = True
                        break
                if not flag:
                    return -1
                count += (j-i)
                t = result.pop(j)
                result.insert(i,t)
        return count
```



![alt text](截屏2026-03-03%2016.07.18.png)



### T20052:最大点数（同2048规则）

dfs, matrices, http://cs101.openjudge.cn/pctbook/T20052/

思路：



代码：

```python
import copy
m,n,p = map(int,input().split())
board = []
for _ in range(m):
    board.append(list(map(int,input().split())))
def left(board):
    m = len(board)
    n = len(board[0])
    while True:
        c = False
        for i in range(m):
            for j in range(n-1, 0, -1):
                if board[i][j] > 0 and board[i][j-1] == 0:
                    # 交换位置，实现数字左移
                    board[i][j], board[i][j-1] = 0, board[i][j]
                    c = True
        if not c:
            break
    # 相同数字合并
    for i in range(m):
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
    # 合并后再次左移，填补合并产生的空位
    while True:
        c = False
        for i in range(m):
            for j in range(n-1, 0, -1):
                if board[i][j] > 0 and board[i][j-1] == 0:
                    board[i][j], board[i][j-1] = 0, board[i][j]
                    c = True
        if not c:
            break
    return board
def rotatel(board):
    m = len(board)
    n = len(board[0])
    return [[board[j][n-1-i] for j in range(m)] for i in range(n)]
def operate(l,board):
    for _ in range(l):
        board = rotatel(board)
    board = left(board)
    for _ in range(3*l):
        board = rotatel(board)
    return board
totalmax = 0
def dfs(board,t):
    totalmax = 0
    for row in board:
        totalmax = max(totalmax,max(row))
    if t == p:
        return totalmax
    for l in range(4):
        board1 = copy.deepcopy(board)
        board1 = operate(l,board1)
        if board1 == board:
            continue
        for row in board1:
            totalmax = max(totalmax,max(row))
        totalmax = max(totalmax,dfs(copy.deepcopy(board1),t+1))
    return totalmax
print(dfs(board,0))
```



![alt text](截屏2026-03-04%2015.36.24.png)





## 2. 学习总结和个人收获
感觉还是浅拷贝深拷贝没有学好，所以最后一道题怎么写都过不了，后面请教了同学和ai才搞清楚
总是感觉人是不是有瓶颈，或者说是我的脑子就是很有上限了，我感觉我已经很久没有那种越过一座大山的爽感了，相反是有一种边际效应的侵蚀，感觉这是在胡思乱想了，总而言之还是希望能把简单中等题做到最好，难题勇于挑战，无愧于心吧
附上leetcode100热题的完结
![alt text](截屏2026-03-04%2016.56.03.png)