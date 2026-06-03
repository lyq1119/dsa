from collections import deque
n = int(input())
mylist = list(map(int,input().split()))
heap = True
if mylist[0] >= mylist[-1]:
    mode = 1
elif mylist[0] < mylist[-1]:
    mode = 2
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
nodes = [TreeNode(mylist[i]) for i in range(n)]
queue = deque([nodes[0]])
i = 0
while queue and i < n:
    node = queue.popleft()
    val = node.val
    i += 1
    if i < n:
        lv = nodes[i].val
        if mode == 1 and val < lv:
            heap = False
        if mode == 2 and val > lv:
            heap = False
        node.left = nodes[i]
        queue.append(nodes[i])
    i += 1
    if i < n:
        rv = nodes[i].val
        if mode == 1 and val < rv:
            heap = False
        if mode == 2 and val > rv:
            heap = False
        node.right = nodes[i]
        queue.append(nodes[i])
def dfs(node,path):
    if not node.right and not node.left:
        print(*path)
        path.pop()
        return
    if node.right:
        path.append(node.right.val)
        dfs(node.right,path)
    if node.left:
        path.append(node.left.val)
        dfs(node.left,path)
    path.pop()
dfs(nodes[0],[nodes[0].val])
if heap:
    if mode == 1:
        print("Max Heap")
    if mode == 2:
        print("Min Heap")
else:
    print("Not Heap")
