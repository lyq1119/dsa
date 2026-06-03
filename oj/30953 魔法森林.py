import sys
sys.setrecursionlimit(100000)
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    graph[b].append(a)
visited = [False]*n
def dfs(a,b):
    visited[a] = b
    for c in graph[a]:
        if visited[c] == False:
            dfs(c,b)
for i in range(n):
    if visited[i] == False:
        dfs(i,i+1)
print(*visited)