import sys
data = iter(sys.stdin.read().split())
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
for _ in range(int(next(data))):
    mystr = next(data)
    n = len(mystr)
    def construct(i,j,mystr):
        if i == j:
            if mystr[i] == "*":
                return
            return TreeNode(mystr[i])
        cur = 0
        t = 0
        for t1 in range(i+1,j+1):
            if mystr[t1] == ")":
                cur -= 1
            elif mystr[t1] == "(":
                cur += 1
            elif cur == 1 and mystr[t1-1] == ",":
                t = t1
                break
        tree = TreeNode(mystr[i])
        tree.left = construct(i+2,t-2,mystr)
        tree.right = construct(t,j-1,mystr)
        return tree
    tree = construct(0,n-1,mystr)
    result1 = []
    result2 = []
    def qianxu(root):
        if root:
            result1.append(root.val)
            qianxu(root.left)
            qianxu(root.right)
    def zhongxu(root):
        if root:
            zhongxu(root.left)
            result2.append(root.val)
            zhongxu(root.right)
    qianxu(tree)
    zhongxu(tree)
    print("".join(result1))
    print("".join(result2))