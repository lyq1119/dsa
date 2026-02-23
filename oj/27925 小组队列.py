import sys
from collections import defaultdict
data = sys.stdin.readlines()
t = int(data[0][:-1])
xiaozuderen = {}
for i in range(t):
    mylist = data[i+1][:-1].split()
    for s in mylist:
        xiaozuderen[s] = i
queue = defaultdict(list)
xiaozu = {i for i in range(t)}
for i in range(t+1,len(data)-1):
    a = data[i][:-1].split()
    if a[0] == "ENQUEUE":
        if a[1] not in xiaozuderen:
            queue[a[1]] = []
        else:
            m = xiaozuderen[a[1]]
            queue[m].append(a[1])
    else:
        b = next(iter(queue))
        if b in xiaozu:
            print(int(queue[b].pop(0)))
            if not queue[b]:
                del queue[b]
        else:
            print(b)
            del queue[b]