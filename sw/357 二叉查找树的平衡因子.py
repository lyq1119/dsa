import sys
data = iter(sys.stdin.read().split())
n = int(next(data))
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
def get_height(node):
    if not node:
        return 0
    return node.height
def insert(tree,node):
    if not tree:
        return node
    cur = tree
    if cur.val > node.val:
        if not cur.left:
            cur.left = node
        else:
            insert(cur.left,node)
        cur.height = max(get_height(cur.left),get_height(cur.right))+1
    else:
        if not cur.right:
            cur.right = node
        else:
            insert(cur.right,node)
        cur.height = max(get_height(cur.left),get_height(cur.right))+1
    return tree
tree = None
for _ in range(n):
    num = int(next(data))
    node = TreeNode(num)
    tree = insert(tree,node)
    bal_factors = []
    def inorder(node):
        if node:
            inorder(node.left)
            bal_factors.append(get_height(node.left)-get_height(node.right))
            inorder(node.right)
    inorder(tree)
print(*bal_factors)

