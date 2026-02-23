import sys
data = list(map(int,sys.stdin.read().split()))
import heapq
n = data[0]
mylist = data[1:]
class Node:
    def __init__(self,weight=0,left=None,right=None):
        self.weight = weight
        self.left = left
        self.right = right
    def __lt__(self,other):
        return self.weight < other.weight
heap = []
for s in mylist:
    heap.append(Node(s))
heapq.heapify(heap)
while len(heap) >= 2:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    node = Node(a.weight+b.weight)
    node.left = a
    node.right = b
    heapq.heappush(heap,node)
tree = heap[0]
def jiaquan(tree,ceng):
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return tree.weight*ceng
    return jiaquan(tree.left,ceng+1)+jiaquan(tree.right,ceng+1)
print(jiaquan(tree,0))