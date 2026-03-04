import sys
data = sys.stdin.read().split()
i = 0
from collections import defaultdict,deque
while i < len(data):
    n = int(data[i])
    i += 1
    huowu = {}
    linjiebiao = defaultdict(set)
    for _ in range(n):
        xq,qian,des = data[i],float(data[i+1]),data[i+2]
        i += 3
        huowu[xq] = qian
        for t in list(des):
            if t == "*":
                linjiebiao[xq].add("e")
                linjiebiao["e"].add(xq)
            else:
                linjiebiao[xq].add(t)
                linjiebiao[t].add(xq)
    queue = deque([(-1,"e")])
    visited = {}
    visited["e"] = 0
    mymax = 0
    while queue:
        step,xq = queue.popleft()
        for xq1 in linjiebiao[xq]:
            if xq1 in visited:
                continue
            visited[xq1] = (0.95**(step+1))*huowu[xq1]
            mymax = max(mymax,visited[xq1])
            queue.append((step+1,xq1))
    print(sorted([xq for xq in visited if visited[xq] == mymax])[0])