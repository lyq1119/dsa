from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
n = int(input())
linjiebiao = defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input().split())
    linjiebiao[a].append(b)
    linjiebiao[b].append(a)
restricted = set(map(int,input().split()))
visited = [False for _ in range(n)]
for num in restricted:
    visited[num] = True
count = 0
def dfs(i):
    global count
    if visited[i]:
        return
    count += 1
    visited[i] = True
    for j in linjiebiao[i]:
        if not visited[j]:
            dfs(j)
dfs(0)
print(count)