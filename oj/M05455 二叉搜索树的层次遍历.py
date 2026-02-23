class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def __init__(self):
        self.tree = None
    def insert(self,s):
        if not self.tree:
            self.tree = TreeNode(s)
            return
        cur = self.tree
        while cur:
            if s < cur.val:
                cur1 = cur
                cur = cur.left
                flag = True
            else:
                cur1 = cur
                cur = cur.right
                flag = False
        if flag:
            cur1.left = TreeNode(s)
        else:
            cur1.right = TreeNode(s)
visited = set()
import sys
mylist = list(map(int,sys.stdin.read().split()))
tree = Tree()
for s in mylist:
    if s in visited:
        continue
    else:
        visited.add(s)
        tree.insert(s)
from collections import deque
queue = deque([tree.tree])
result = []
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
print(*result)