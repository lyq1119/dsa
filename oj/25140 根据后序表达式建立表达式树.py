import sys
data = iter(sys.stdin.read().split())
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
for _ in range(int(next(data))):
    mystr = list(next(data))
    stack = []
    for s in mystr:
        node = TreeNode(s)
        if s.isupper():
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    tree = stack[0]
    result = []
    from collections import deque
    queue = deque([tree])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    print("".join(reversed(result)))