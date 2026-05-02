N = int(input())
mylist = list(map(int,input().split()))
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def construct(i,node):
    if 2*i <= N:
        node.left = construct(2*i,TreeNode(mylist[2*i-1]))
    if 2*i+1 <= N:
        node.right = construct(2*i+1,TreeNode(mylist[2*i]))
    return node
root = construct(1,TreeNode(mylist[0]))
def find(node):
    if not node:
        return 0
    total1 = node.val
    if node.left:
        total1 += find(node.left.left)
        total1 += find(node.left.right)
    if node.right:
        total1 += find(node.right.left)
        total1 += find(node.right.right)
    total2 = find(node.left) + find(node.right)
    return max(total1,total2)
print(find(root))