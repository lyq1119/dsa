n,m = map(int,input().split())
weight = list(map(int,input().split()))
class Vertice:
    def __init__(self,val):
        self.val = val
        self.neighbors = set()
class Graph:
    def __init__(self):
        self.vertices = {i:Vertice(i) for i in range(n)}
    def addedge(self,i,j):
        i = self.vertices[i]
        j = self.vertices[j]
        i.neighbors.add(j)
        j.neighbors.add(i)
graph = Graph()
for _ in range(m):
    i,j = map(int,input().split())
    graph.addedge(i,j)
visited = set()
def dfs(i):
    total = weight[i]
    i = graph.vertices[i]
    for t in i.neighbors:
        if t not in visited:
            visited.add(t)
            total += dfs(t.val)
    return total
maximum = 0
for i in range(n):
    if graph.vertices[i] not in visited:
        visited.add(graph.vertices[i])
        a = dfs(i)
        maximum = max(maximum,a)
print(maximum)