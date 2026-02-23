n,m = map(int,input().split())
mydict = {}
for _ in range(m):
    u,v = map(int,input().split())
    mydict[u] = mydict.get(u,0)+1
    mydict[v] = mydict.get(v,0)+1
for i in range(n):
    if i < n-1:
        print(mydict[i],end=" ")
    else:
        print(mydict[i])