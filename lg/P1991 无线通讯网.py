s,p = map(int,input().split())
mylist = []
for _ in range(p):
    x,y = map(int,input().split())
    mylist.append((x,y))
edges = []
def dist(i,j):
    a,b = mylist[i]
    c,d = mylist[j]
    return (a-c)**2 + (b-d)**2
graph = [[0]*p for _ in range(p)]
for i in range(p):
    for j in range(i,p):
        distance = dist(i,j)
        edges.append((distance,i,j))
        edges.append((distance,j,i))
        graph[i][j] = distance
        graph[j][i] = distance
def kruskal(n, edges):
    # 按权重从小到大排序
    edges.sort()
    # 初始化 parent 数组（代替类的 self.parent）
    parent = list(range(n))
    parent = [i for i in range(n)]
    cc = n
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])  # 路径压缩
        return parent[i]
    def union(i, j):
        nonlocal cc
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            cc -= 1
    for w,u,v in edges:
        union(u, v)
        if cc <= s:
            res = w
            break
    print(f"{res**(0.5):.2f}")
kruskal(p,edges)     