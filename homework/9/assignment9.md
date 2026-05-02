# DSA Assignment #9: 图（1/3）
2500010774 兰玉琪 数学科学学院

## 1. 题目
### M28046: 词梯
bfs, http://cs101.openjudge.cn/practice/28046/
思路：
代码：
```python
import sys
from collections import defaultdict,deque
data = iter(sys.stdin.read().split())
n = int(next(data))
buckets = defaultdict(list)
linjiebiao = defaultdict(set)
for _ in range(n):
    word = next(data)
    for i in range(4):
        bucket = word[:i]+"_"+word[(i+1):]
        for neighbor in buckets[bucket]:
            linjiebiao[word].add(neighbor)
            linjiebiao[neighbor].add(word)
        buckets[bucket].append(word)
begin,end = next(data),next(data)
queue = deque([begin])
visited = {begin}
prev = {begin:None}
flag = False
while queue:
    word = queue.popleft()
    if word == end:
        flag = True
        cur = end
        result = []
        while prev[cur]:
            result.append(cur)
            cur = prev[cur]
        result.append(begin)
        print(*list(reversed(result)))
        break
    for neighbor in linjiebiao[word]:
        if neighbor not in visited:
            queue.append(neighbor)
            prev[neighbor] = word
            visited.add(neighbor)
if not flag:
    print("NO")
```
![alt text](截屏2026-05-01%2019.37.45.png)
### M433.最小基因变化
bfs, https://leetcode.cn/problems/minimum-genetic-mutation/
思路：
代码：
```python
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        from collections import deque
        q = deque([(startGene,0)])
        visited = {startGene}
        tihuans = ["A","C","G","T"]
        while q:
            gene,step = q.popleft()
            if gene == endGene:
                return step        
            for i in range(8):
                for tihuan in tihuans:
                    gene1 = list(gene)
                    gene1[i] = tihuan
                    gene1 = "".join(gene1)
                    if gene1 not in visited and gene1 in bank:
                        q.append((gene1,step+1))
                        visited.add(gene1)
        return -1
```
![alt text](截屏2026-05-01%2019.41.38.png)
### sy382: 有向图判环 中等
Karn, dfs, Floyd-Warshall, https://sunnywhy.com/sfbj/10/3/382
思路：
五一要好好学习了，所以三种方法都写
代码：
法一:Karn(DFS+递归栈标记)
```python
import sys
from collections import defaultdict
data = iter(sys.stdin.read().split())
n,m = int(next(data)),int(next(data))
linjiebiao = defaultdict(list)
verdict = False
for _ in range(m):
    linjiebiao[int(next(data))].append(int(next(data)))
visited = [False for _ in range(n)]
curpath = [False for _ in range(n)]
def dfs(i):
    global verdict
    if curpath[i]:
        verdict = True
        return
    curpath[i] = True
    visited[i] = True
    for j in linjiebiao[i]:
        dfs(j)
    curpath[i] = False
for i in range(n):
    if visited[i] == False:
        dfs(i)
    if verdict:
        break
if verdict:
    print("Yes")
else:
    print("No")
```
法二:拓扑排序
```python
from collections import deque
n,m = map(int,input().split())
class Vertice:
    def __init__(self,val):
        self.val = val
        self.neighbors = set()
        self.rudu = 0
class Graph:
    def __init__(self):
        self.vertices = {i:Vertice(i) for i in range(n)}
    def addedge(self,i,j):
        i = self.vertices[i]
        j = self.vertices[j]
        i.neighbors.add(j)
        j.rudu += 1
graph = Graph()
for _ in range(m):
    i,j = map(int,input().split())
    graph.addedge(i,j)
def tuopu():
    queue = deque([])
    for i in range(n):
        if not graph.vertices[i].rudu:
            queue.append(graph.vertices[i])
    count = len(graph.vertices)
    while queue:
        t = queue.popleft()
        count -= 1
        for s in t.neighbors:
            s.rudu -= 1
            if not s.rudu:
                queue.append(s)
    if count:
        return True
    return False
if tuopu():
    print("Yes")
else:
    print("No")
```
法三：Floyd-Warshall
这个懒得用python了，直接给c++练个手
```cpp
#include <iostream>
#include <vector>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    int a, b;
    bool verdict{false};
    cin >> n >> m;

    vector<vector<bool>> matrix;

    matrix.resize(n);
    for (vector<bool>& mylist : matrix){
        mylist.resize(n);
    }

    for (int i = 0; i < n; i++){
        matrix[i][i] = true;
    }

    for (int i = 0; i < m; i++){
        cin >> a >> b;
        matrix[a][b] = true;
        if (matrix[b][a]){
            verdict = true;
            break;
        }
    }

    if (verdict){
        cout << "Yes" << endl;
        return 0;
    }
    
    for (int k = 0; k < n; k++){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (j == i){
                    continue;
                }
                if (matrix[i][k] && matrix[k][j]){
                    matrix[i][j] = true;
                    if (matrix[j][i]){
                        verdict = true;
                        cout << "Yes" << endl;
                        return 0;
                    }
                }
            }
        }
    }

    cout << "No" << endl;
    return 0;
}
```
![alt text](截屏2026-05-02%2000.06.54.png)
### M909.蛇梯棋
bfs, https://leetcode.cn/problems/snakes-and-ladders/
思路：
代码：
```python
class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        from collections import deque
        board1 = {}
        for i in range(n):
            if i % 2 == 0:
                for j in range(1,n+1):
                    board1[n*i+j] = (n-1-i,j-1)
            else:
                for j in range(n):
                    board1[n*(i+1)-j] = (n-1-i,j)
        q = deque([(1,0)])
        visited = {1}
        while q:
            num,step = q.popleft()
            if num == n**2:
                return step
            for t in range(1,7):
                if num+t <= n**2:
                    a,b = board1[num+t]
                    if num+t not in visited and board[a][b] == -1:
                        q.append((num+t,step+1))
                        visited.add(num+t)
                    elif board[a][b] != -1:
                        if board[a][b] not in visited:
                            visited.add(board[a][b])
                            q.append((board[a][b],step+1))
        return -1
```
![alt text](截屏2026-05-02%2000.09.25.png)
### M28050: 骑士周游
dfs, http://cs101.openjudge.cn/practice/28050/
思路：
代码
```python
n = int(input())
x,y = map(int,input().split())
vector = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
def available(lc):
    mylist = []
    for myvector in vector:
        a,b = lc[0]+myvector[0],lc[1]+myvector[1]
        if a >= 0 and a <= n-1 and b >= 0 and b <= n-1:
            mylist.append((a,b))
    return mylist
def count(lc,myset):
    count = 0
    for t in available(lc):
        if t not in myset:
            count += 1
    return count
def choose(mylist,myset):
    mylist.sort(key=lambda x:count(x,myset))
    return mylist
def backtrack(lc,myset):
    if len(myset) == n*n:
        return True
    mylist = choose(available(lc),myset)
    for lc1 in mylist:
        if lc1 not in myset:
            myset.add(lc1)
            a = backtrack(lc1,myset)
            if a:
                myset.discard(lc1)
                return True
            myset.discard(lc1)
    return False
if backtrack((x,y),{(x,y)}):
    print("success")
else:
    print("fail")
```
![alt text](截屏2026-05-02%2000.10.39.png)

### T37.解数独
backtracking, hash table, https://leetcode.cn/problems/sudoku-solver/
思路：
代码
```python
class Solution:
    def solveSudoku(self, board) -> None:
        hang,lie,kuai = [0 for _ in range(9)],[0 for _ in range(9)],[0 for _ in range(9)]
        vac = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    vac.add((i,j))
        def update(i,j):
            num = 0
            num = num|hang[i]|lie[j]|kuai[3*(i//3)+(j//3)]
            return num
        def findmin():
            i1,j1 = 10,10
            maxnum = -1
            for i,j in vac:
                a = update(i,j)
                if a > maxnum:
                    i1,j1 = i,j
                    maxnum = a
            return i1,j1
        def uplin(i,j):
            a = int(board[i][j])
            hang[i] = hang[i]|(1<<a)
            lie[j] = lie[j]|(1<<a)
            kuai[3*(i//3)+(j//3)] = kuai[3*(i//3)+(j//3)]|(1<<a)
        def downlin(i,j):
            a = int(board[i][j])
            a = 1022-(1<<a)
            hang[i] = hang[i]&a
            lie[j] = lie[j]&a
            kuai[3*(i//3)+(j//3)] = kuai[3*(i//3)+(j//3)]&a
        for i in range(9):
            for j in range(9):
                if (i,j) not in vac:
                    uplin(i,j)
        i,j = findmin()
        def dfs(i,j):
            if i == 10:
                return True
            m = update(i,j)
            for s in range(1,10):
                t = (1<<s)|m
                if t == m:
                    continue
                board[i][j] = str(s)
                uplin(i,j)
                vac.discard((i,j))
                i1,j1 = findmin()  
                if dfs(i1,j1):
                    return True
                downlin(i,j)
                board[i][j] = "."
                vac.add((i,j))
            return False
        dfs(i,j)
```
![alt text](截屏2026-05-02%2000.12.05.png)

## 2. 学习总结和个人收获
我这该死的拖延症，一直不好好学c++，始终水平就是已读，已尝试在ai的辅助下把这次作业非tough的题用c++写了一遍
