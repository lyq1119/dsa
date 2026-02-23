n,m = map(int,input().split())
mydict1 = {}
mydict2 = {}
for _ in range(m):
    u,v = map(int,input().split())
    mydict1[u] = mydict1.get(u,0)+1
    mydict2[v] = mydict2.get(v,0)+1
for i in range(n):
    print(mydict2.get(i,0),mydict1.get(i,0))