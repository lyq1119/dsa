import sys
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.height = 1
        self.left = None
        self.right = None
def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    tree = None
    def get_height(node):
        if not node:
            return 0
        return node.height
    def rightrotate(node):
        root = node.left
        node1 = node.left.right
        root.right = node
        node.left = node1
        node.height = max(get_height(node.left),get_height(node.right))+1
        root.height = max(get_height(root.left),get_height(root.right))+1
        return root
    def leftrotate(node):
        root = node.right
        node1 = node.right.left
        root.left = node
        node.right = node1
        node.height = max(get_height(node.left),get_height(node.right))+1
        root.height = max(get_height(root.left),get_height(root.right))+1
        return root
    def insert(node,val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = insert(node.left,val)
        else:
            node.right = insert(node.right,val)
        node.height = max(get_height(node.left),get_height(node.right))+1
        balance = get_height(node.left)-get_height(node.right)
        if balance > 1:
            if val < node.left.val:
                node = rightrotate(node)
            else:
                node.left = leftrotate(node.left)
                node = rightrotate(node)
        elif balance < -1:
            if val > node.right.val:
                node = leftrotate(node)
            else:
                node.right = rightrotate(node.right)
                node = leftrotate(node)
        return node
    for i in range(1,n+1):
        tree = insert(tree,int(data[i]))
    result = []
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    preorder(tree)
    print(*result)
if __name__ == "__main__":
    solve()