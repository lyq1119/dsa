from collections import defaultdict
n,m = map(int,input().split())
costs = list(map(int,input().split()))
linjiebiao = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    linjiebiao[a].append(b)
    linjiebiao[b].append(a)
visited = [False] * n
def dfs(i):
    if visited[i]:
        return float("inf")
    curmin = costs[i]
    visited[i] = True
    for j in linjiebiao[i]:
        curmin = min(curmin,dfs(j))
    return curmin
total = 0
for i in range(n):
    if not visited[i]:
        total += dfs(i)
print(total)