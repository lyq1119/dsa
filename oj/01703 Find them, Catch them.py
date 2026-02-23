import sys
data = sys.stdin.read().split()
t = 0
T = int(data[t])
t += 1
for _ in range(T):
    n,m = int(data[t]),int(data[t+1])
    t += 2
    Parent = [i for i in range(n)]
    Type = [0 for i in range(n)]
    def find(i):
        if (Parent[i] == i):
            return i
        else:
            result = find(Parent[i])
            Type[i] = (Type[i]+Type[Parent[i]])%2
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
            Type[i1] = (-Type[i]+1+Type[j])%2
        elif rank[i1] >= rank[j1]:
            Parent[j1] = i1
            Type[j1] = (-Type[j]+1+Type[i])%2
        rank[i1] += 1
    for __ in range(m):
        verdict,case1,case2 = data[t],int(data[t+1]),int(data[t+2])
        if verdict == "A":
            i1 = find(case1-1)
            i2 = find(case2-1)
            if i1 != i2:
                print('Not sure yet.')
            else:
                if Type[case1-1] == Type[case2-1]:
                    print('In the same gang.')
                else:
                    print('In different gangs.')
        else:
            union(case1-1,case2-1)
        t += 3
