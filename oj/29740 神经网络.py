from collections import deque
n,p = map(int,input().split())
matrix = [[0]*n for _ in range(n)]
has_edge = [[False]*n for _ in range(n)]
c_state = []
bias = []
for _ in range(n):
    c,u = map(int,input().split())
    c_state.append(c)
    bias.append(u)
indegree = [0]*n
outdegree = [0]*n
num_visited = 0
queue = deque()
shuru = set()
for _ in range(p):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    matrix[u][v] += w
    if has_edge[u][v]:
        continue
    has_edge[u][v] = True
    indegree[v] += 1
    outdegree[u] += 1
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)
        shuru.add(i)
while queue:
    u = queue.popleft()
    num_visited += 1
    for v in range(n):
        if has_edge[u][v]:
            indegree[v] -= 1
            if c_state[u] > 0:
                c_state[v] += c_state[u] * matrix[u][v]
            if indegree[v] == 0:
                c_state[v] = c_state[v]-bias[v]
                queue.append(v)
if num_visited != n:
    print("NULL")
else:
    shuchu = [c_state[i] for i in range(n) if outdegree[i] == 0]
    if max(shuchu) <= 0:
        print("NULL")
    else:
        for i in range(n):
            if not outdegree[i] and c_state[i] > 0:
                print(i+1,c_state[i])