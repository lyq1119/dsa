n = int(input())
result = []
class TreeNode:
    def __init__(self,val=0):
        self.val = val
        self.children = []
from collections import deque
for _ in range(n):
    mylist = input().split()
    i = 2
    dummy = TreeNode()
    dummy.children = [TreeNode(mylist[0])]
    queue = deque([(dummy.children[0],int(mylist[1]))])
    while queue:
        node,node_num = queue.popleft()
        for _ in range(node_num):
            value = mylist[i]
            node_num = int(mylist[i+1])
            i += 2
            newnode = TreeNode(value)
            queue.append((newnode,node_num))
            node.children.append(newnode)
    def houxu(node):
        if node:
            for newnode in node.children:
                houxu(newnode)
            result.append(node.val)
    houxu(dummy.children[0])
print(*result)
        