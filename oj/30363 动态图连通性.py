n,m = map(int,input().split())
graph = []
Parent = [i for i in range(n)]
size = [1]*n
def find(i):
    if (Parent[i] == i):
        return i
    else:
        result = find(Parent[i])
        Parent[i] = result
        return result
def union(i,j):
    x = find(i)
    y = find(j)
    if x == y:
        return 0
    Parent[y] = x
    t = size[x]
    size[x] += size[y]
    return (size[x])*(size[x]-1)//2 - t*(t-1)//2 - size[y]*(size[y]-1)//2
total = 0
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    total += union(a,b)
    print(total)