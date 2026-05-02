import math
n = int(input())
mylist = list(map(int,input().split()))
k = int(math.log2(n))
for i in range(k,0,-1):
    gap = 2**i-1
    for j in range(n-gap):
        for t in range(j+gap,n,gap):
            if mylist[j] > mylist[t]:
                mylist[j],mylist[t] = mylist[t],mylist[j]
    print(*mylist)