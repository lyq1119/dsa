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
graph = Graph()
for _ in range(m):
    i,j = map(int,input().split())
    graph.addedge(i,j)
visited = set()
stack = set()
def dfs(i):
    i = graph.vertices[i]
    stack.add(i)
    for t in i.neighbors:
        if t in stack:
            return True
        if t not in visited:
            visited.add(t)
            stack.add(t)
            verdict = dfs(t.val)
            if verdict:
                return True
    stack.discard(i)
    return False
def solve():
    for i in range(n):
        if graph.vertices[i] not in visited:
            visited.add(graph.vertices[i])
            if dfs(i):
                return True
    return False
if solve():
    print("Yes")
else:
    print("No")