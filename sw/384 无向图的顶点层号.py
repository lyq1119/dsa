from collections import deque
n,m,s = map(int,input().split())
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
def bfs():# visited 和 queue 都存数字
    ceng = [0]*n
    queue = deque([(s,0)])
    visited = {s}
    while queue:
        t,step = queue.popleft()
        ceng[t] = step
        for l in graph.vertices[t].neighbors:
            if l.val not in visited:
                visited.add(l.val)
                queue.append((l.val,step+1))
    print(*ceng)
bfs()