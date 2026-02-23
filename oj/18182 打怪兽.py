import sys
data = sys.stdin.read().split()
from collections import defaultdict
i = 1
for _ in range(int(data[0])):
    n,m,b = int(data[i]),int(data[i+1]),int(data[i+2])
    i += 3
    mydict = defaultdict(list)
    siqushijian = -1
    for __ in range(n):
        t,x = int(data[i]),int(data[i+1])
        mydict[t].append(x)
        i += 2
    flag = True
    for t in sorted([key for key in mydict]):
        ge = 0
        for x in sorted(mydict[t],reverse=True):
            b -= x
            if b <= 0:
                siqushijian = t
                flag = False
                break
            ge += 1
            if ge >= m:
                break
        if not flag:
            break
    if siqushijian == -1:
        print("alive")
    else:
        print(siqushijian)