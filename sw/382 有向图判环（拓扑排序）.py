from collections import deque
n,m = map(int,input().split())
class Vertice:
    def __init__(self,val):
        self.val = val
        self.neighbors = set()
        self.rudu = 0
class Graph:
    def __init__(self):
        self.vertices = {i:Vertice(i) for i in range(n)}
    def addedge(self,i,j):
        i = self.vertices[i]
        j = self.vertices[j]
        i.neighbors.add(j)
        j.rudu += 1
graph = Graph()
for _ in range(m):
    i,j = map(int,input().split())
    graph.addedge(i,j)
def tuopu():
    queue = deque([])
    for i in range(n):
        if not graph.vertices[i].rudu:
            queue.append(graph.vertices[i])
    count = len(graph.vertices)
    while queue:
        t = queue.popleft()
        count -= 1
        for s in t.neighbors:
            s.rudu -= 1
            if not s.rudu:
                queue.append(s)
    if count:
        return True
    return False
if tuopu():
    print("Yes")
else:
    print("No")