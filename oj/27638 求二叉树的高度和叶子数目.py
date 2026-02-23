import sys
data = iter(sys.stdin.read().split())
mylist = []
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
for _ in range(int(next(data))):
    a = int(next(data))
    b = int(next(data))
    mylist.append((a,b))
def construct(mylist):
    n = len(mylist)
    nodes = [TreeNode(i) for i in range(n)]
    visited = set()
    for k in range(n):
        a,b = mylist[k]
        if a != -1:
            visited.add(a)
            nodes[k].left = nodes[a]
        if b != -1:
            visited.add(b)
            nodes[k].right = nodes[b]
    for i in range(n):
        if i not in visited:
            break
    return nodes[i]
tree = construct(mylist)
def searchdepth(node):
    if not node:
        return -1
    a = searchdepth(node.left)
    b = searchdepth(node.right)
    return max(a,b) + 1
def yezishu(node):
    if not node.left and not node.right:
        return 1
    shumu = 0
    if node.left:
        shumu += yezishu(node.left)
    if node.right:
        shumu += yezishu(node.right)
    return shumu
print(searchdepth(tree),yezishu(tree))