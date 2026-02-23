import sys
data = sys.stdin.read().split()
zhong,hou = list(data[0]),list(data[1])
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def construct(i,j,k,l,zhong,hou):
    if i > j:
        return
    root = TreeNode(hou[j])
    a = zhong.index(hou[j])
    t = a-k
    root.left = construct(i,i+t-1,k,k+t-1,zhong,hou)
    root.right = construct(i+t,j-1,a+1,l,zhong,hou)
    return root
tree = construct(0,len(zhong)-1,0,len(hou)-1,zhong,hou)
result = []
def qianxu(tree):
    if tree:
        result.append(tree.val)
        qianxu(tree.left)
        qianxu(tree.right)
qianxu(tree)
print("".join(result))