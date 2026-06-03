import sys
sys.setrecursionlimit(10000)
from collections import defaultdict
n = int(input())
kuaile = []
linjiebiao = defaultdict(list)
for _ in range(n):
    kuaile.append(int(input()))
feigen = set()
for _ in range(n-1):
    a,b = map(int,input().split())
    b -= 1
    a -= 1
    linjiebiao[b].append(a)
    feigen.add(a)
for i in range(n):
    if i not in feigen:
        root = i
def dfs(i):
    if not linjiebiao[i]:
        return max(0,kuaile[i])
    a1 = 0
    for j in linjiebiao[i]:
        t = dfs(j)
        a1 += max(t,0)
    a2 = max(0,kuaile[i])
    for j in linjiebiao[i]:
        for k in linjiebiao[j]:
            a2 += max(dfs(k),0)
    return max(a1,a2)
print(dfs(root))