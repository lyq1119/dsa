n = int(input())
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
for _ in range(n):
    cur = [None for __ in range(100)]
    while True:
        s = input()
        if s == "0":
            break
        cur[len(s)-1] = TreeNode(s[-1])
        if len(s) == 1:
            continue
        parent = cur[len(s)-2]
        if parent.left:
            parent.right = cur[len(s)-1]
        else:
            parent.left = cur[len(s)-1]
    root = cur[0]
    list1 = []
    def preorder(node):
        if not node or node.val == "*":
            return
        list1.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    print("".join(list1))
    list3 = []
    def postorder(node):
        if not node or node.val == "*":
            return
        postorder(node.left)
        postorder(node.right)
        list3.append(node.val)
    postorder(root)
    print("".join(list3))
    list2 = []
    def inorder(node):
        if not node or node.val == "*":
            return
        inorder(node.left)
        list2.append(node.val)
        inorder(node.right)
    inorder(root)
    print("".join(list2))
    if _ != n-1:
        print("")