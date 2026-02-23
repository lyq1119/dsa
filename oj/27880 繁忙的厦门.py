n,m = map(int,input().split())
edges = []
for _ in range(m):
    u,v,weight = map(int,input().split())
    edges.append([weight,u-1,v-1])
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False
def kruskal(n, edges):
    # 按权重从小到大排序
    edges.sort()
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = 0
    for weight, u, v in edges:
        # 尝试合并：如果合并成功，说明没有环
        if uf.union(u, v):
            mst_weight = max(weight,mst_weight)
            mst_edges += 1
            # 如果已经找够了 n-1 条边，可以提前结束
            if mst_edges == n-1:
                break
    return mst_weight
b = kruskal(n,edges)
print(n-1,b)