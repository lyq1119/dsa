from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = []
def postorder(node,res):
    if node:
        for child in node.children:
            res = postorder(child,res)
        res.append(node.val)
    return res
def solve():
    mylist = input().split()
    root = TreeNode(mylist[0])
    q = deque([(root,int(mylist[1]))])
    i = 0
    while q:
        for _ in range(len(q)):
            node,num_children = q.popleft()
            for __ in range(num_children):
                i += 2
                nodechild = TreeNode(mylist[i])
                num = int(mylist[i+1])
                node.children.append(nodechild)
                q.append((nodechild, num))
    return postorder(root,[])
res = []
for _ in range(int(input())):
    res += solve()
print(*res)