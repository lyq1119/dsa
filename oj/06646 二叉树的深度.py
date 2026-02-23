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
    nodes = [TreeNode(i) for i in range(n+1)]
    for k in range(n):
        a,b = mylist[k]
        if a != -1:
            nodes[k+1].left = nodes[a]
        if b != -1:
            nodes[k+1].right = nodes[b]
    return nodes[1]
def searchdepth(node):
    if not node:
        return 0
    a = searchdepth(node.left)
    b = searchdepth(node.right)
    return max(a,b) + 1
tree = construct(mylist)
print(searchdepth(tree))
