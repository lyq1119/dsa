n,m = map(int,input().split())
Parent = [i for i in range(n)]
type = [0]*n
def find(i):
    if (Parent[i] == i):
        return i
    else:
        result = find(Parent[i])
        type[i] = (type[i]+type[Parent[i]])%2 #这里是找以前的父节点，后面率先更新的type应该是以前的父节点
        Parent[i] = result
        return result
def union(i,j,k):
    x = find(i)
    y = find(j)
    if x == y:
        return (type[j] - type[i])%2 == k
    Parent[y] = x
    type[y] = (k+type[i]-type[j])%2
    return True
verdict = True
for _ in range(m):
    a,b,c = map(int,input().split())
    verdict = verdict and union(a,b,c)
if verdict:
    print("YES")
else:
    print("NO")