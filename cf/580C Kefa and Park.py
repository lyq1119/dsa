import sys
data = iter(sys.stdin.read().split())
n = int(next(data))
m = int(next(data))
nodes = []
class Treenode:
    def __init__(self,i,mao):
        self.index = i
        self.mao = mao
        self.neighbors = set()
for i in range(n):
    node = Treenode(i,int(next(data)))
    nodes.append(node)
from collections import defaultdict,deque
mydict = defaultdict(set)
for _ in range(n-1):
    a = int(next(data))-1
    b = int(next(data))-1
    mydict[a].add(b)
    mydict[b].add(a)
visited = {0}
queue = deque([0])
while queue:
    i = queue.popleft()
    for j in mydict[i]:
        if j not in visited:
            nodes[i].neighbors.add(j)
            queue.append(j)
            visited.add(j) 
nums = [0 for _ in range(n)]
def bfs():
    count = 0
    queue = deque([0])
    nums[0] = nodes[0].mao
    while queue:
        i = queue.popleft()
        node = nodes[i]
        if not node.neighbors:
            count += 1
            continue
        if not node.mao:
            for t in node.neighbors:
                nums[t] = nodes[t].mao
                queue.append(t)
        else:
            for t in node.neighbors:
                if nodes[t].mao:
                    if 1+nums[i] > m:
                        continue
                    nums[t] = 1+nums[i]
                else:
                    nums[t] = 0
                queue.append(t)
    print(count)
bfs()

