n,m,s,k = map(int,input().split())
from collections import deque
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
def bfs():# visited 和 queue 都存数字
    count = 0
    queue = deque([(s,0)])
    visited = {s}
    while queue:
        t,step = queue.popleft()
        if step > k:
            break
        count += 1
        for l in graph.vertices[t].neighbors:
            if l.val not in visited:
                visited.add(l.val)
                queue.append((l.val,step+1))
    print(count)
bfs()