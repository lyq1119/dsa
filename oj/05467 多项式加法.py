import sys
from collections import defaultdict
data = sys.stdin.read().split()
n = int(data[0])
i = 1
for _ in range(n):
    mydict = defaultdict(int)
    while i < len(data):
        a,b = int(data[i]),int(data[i+1])
        if b < 0:
            i += 2
            break
        mydict[b] += a
        i += 2
    while i < len(data):
        a,b = int(data[i]),int(data[i+1])
        if b < 0:
            i += 2
            break
        mydict[b] += a
        i += 2
    result = []
    for cishu in sorted(mydict,reverse=True):
        if mydict[cishu]:
            result.append(f"[ {mydict[cishu]} {cishu} ]")
    print(" ".join(result))

