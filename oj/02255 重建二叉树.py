import sys
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def construct(i,j,k,l,qian,zhong):
    if i > j:
        return
    root = TreeNode(qian[i])
    a = zhong.index(qian[i])
    t = a-k
    root.left = construct(i+1,i+t,k,k+t-1,qian,zhong)
    root.right = construct(i+t+1,j,a+1,l,qian,zhong)
    return root 
def houxu(tree):
    if tree:
        houxu(tree.left)
        houxu(tree.right)  
        result.append(tree.val)
data = sys.stdin.read().split()
for i in range(len(data)//2):
    qian,zhong = list(data[2*i]),list(data[2*i+1])
    tree = construct(0,len(qian)-1,0,len(zhong)-1,qian,zhong)
    result = []
    houxu(tree)
    print("".join(result))