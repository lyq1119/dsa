import sys
data = iter(sys.stdin.read().split())
n = int(next(data))
import heapq
class Node:
    def __init__(self,weight=0,zimu=set(),left=None,right=None):
        self.weight = weight
        self.zimu = zimu
        self.left = left
        self.right = right
    def __lt__(self,other):
        if self.weight != other.weight:
            return self.weight < other.weight
        return self.zimu < other.zimu
heap = []
mydict = {}
for _ in range(n):
    zimu = next(data)
    weight = int(next(data))
    node = Node(weight,{zimu})
    mydict[zimu] = ""
    heap.append(node)
heapq.heapify(heap)
while len(heap) >= 2:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    for s in a.zimu:
        mydict[s] = "0"+mydict[s]
    for s in b.zimu:
        mydict[s] = "1"+mydict[s]
    node = Node(a.weight+b.weight,a.zimu|b.zimu)
    node.left = a
    node.right = b
    heapq.heappush(heap,node)
tree = heap[0]
result = []
def jiema(num):
    i = 0
    cur = tree
    result = []
    while i <= len(num)-1:
        if num[i] == '0':
            if cur.left:
                cur = cur.left
                i += 1
            else:
                result.append(list(cur.zimu)[0])
                cur = tree.left
                i += 1
        else:
            if cur.right:
                cur = cur.right
                i += 1
            else:
                result.append(list(cur.zimu)[0])
                cur = tree.right
                i += 1
    result.append(list(cur.zimu)[0])
    return "".join(result)
while True:
    try:
        a = next(data)
        if a[0].isdigit():
            print(jiema(a))
        else:
            print("".join([mydict[s] for s in a]))
    except StopIteration:
        break
