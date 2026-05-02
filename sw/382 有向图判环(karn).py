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