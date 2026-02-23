from collections import defaultdict
n,m = map(int,input().split())
linjiebiao = defaultdict(list)
for _ in range(m):
    t,s = map(int,input().split())
    linjiebiao[t].append(s)
    linjiebiao[s].append(t)
for i in range(n):
    mylist = [f"{i}({len(linjiebiao[i])})"]+linjiebiao[i]
    print(*mylist)