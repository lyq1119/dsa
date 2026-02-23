import sys
data = sys.stdin.read().split()
i = 0
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
seq = []
while i < len(data):
    if data[i] == "$" or data[i] == "*":
        def insert(node,s):
            if not node:
                node = TreeNode(s)
                return
            cur = node
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
        tree = TreeNode(seq.pop())
        while seq:
            for s in list(seq.pop()):
                insert(tree,s)
        result = []
        def preorder_traversal(node):
            if node:
                result.append(node.val)
                preorder_traversal(node.left)
                preorder_traversal(node.right)
        preorder_traversal(tree)
        print("".join(result))
        seq = []
        if data[i] == "$":
            break
    else:
        seq.append(data[i])
    i += 1