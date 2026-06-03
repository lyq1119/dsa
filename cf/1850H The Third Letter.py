import sys
sys.setrecursionlimit(200000)
def solve():
    n,m = map(int,input().split())
    Parent = [i for i in range(n)]
    type = [0]*n
    def find(i):
        if (Parent[i] == i):
            return i
        else:
            result = find(Parent[i])
            type[i] = type[i]+type[Parent[i]] #这里是找以前的父节点，后面率先更新的type应该是以前的父节点
            Parent[i] = result
            return result
    def union(i,j,k):
        x = find(i)
        y = find(j)
        if x == y:
            return type[j] - type[i] == k
        Parent[y] = x
        type[y] = (k+type[i]-type[j])
        return True
    verdict = True
    for _ in range(m):
        i,j,k = map(int,input().split())
        i -= 1
        j -= 1
        verdict = verdict and union(i,j,k)
    return verdict
for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")