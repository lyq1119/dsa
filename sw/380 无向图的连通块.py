n,m = map(int,input().split())
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
    i = graph.vertices[i]
    for t in i.neighbors:
        if t not in visited:
            visited.add(t)
            dfs(t.val)
count = 0
for i in range(n):
    if graph.vertices[i] not in visited:
        count += 1
        dfs(i)
print(count)