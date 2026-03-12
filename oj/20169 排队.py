for _ in range(int(input())):
    n,m = map(int,input().split())
    Parent = [i for i in range(n)]
    def find(i):
        if (Parent[i] == i):
            return i
        else:
            result = find(Parent[i])
            Parent[i] = result
            return result
    def union(i,j):
        i1 = find(i)
        j1 = find(j)
        if i1 == j1:
            return
        Parent[i1] = j1
    for __ in range(m):
        i,j = map(int,input().split())
        union(i-1,j-1)
    print(*[find(i)+1 for i in range(n)])