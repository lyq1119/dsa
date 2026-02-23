import sys
data = sys.stdin.read().split()
i = 0
while True:
    if data[i] == '0' and data[i+1] == '0':
        break
    n,m = int(data[i]),int(data[i+1])
    i += 2
    Parent = [i for i in range(n)]
    def find(i):
        if (Parent[i] == i):
            return i
        else:
            result = find(Parent[i])
            Parent[i] = result
            return result
    rank = [1]*n
    def union(i,j):
        i1 = find(i)
        j1 = find(j)
        if i1 == j1:
            return
        if rank[i1] < rank[j1]:
            Parent[i1] = j1
        elif rank[i1] > rank[j1]:
            Parent[j1] = i1
        else:
            Parent[j1] = i1
            rank[i1] += 1
    for _ in range(m):
        num = int(data[i])
        i += 1
        for t in range(i,i+num-1):
            union(int(data[t]),int(data[t+1]))
        i += num
    root = find(0)
    Parent = [find(i) for i in range(n)]
    print(Parent.count(root))