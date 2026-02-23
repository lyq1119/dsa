import sys
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def solve():
    data = list(map(int,sys.stdin.read().split()))
    n = data[0]
    qianxu = data[1:]
    def construct(i,k):
        if i > k:
            return
        num = qianxu[i]
        node = TreeNode(num)
        flag = False
        for j in range(i+1,k+1):
            if qianxu[j] > num:
                flag = True
                break
        if not flag:
            j = k+1
        node.left = construct(i+1,j-1)
        node.right = construct(j,k)
        return node  
    tree = construct(0,n-1)
    result = []
    def houxu(node):
        if node:
            houxu(node.left)
            houxu(node.right)
            result.append(node.val)
    houxu(tree)
    print(*result)
if __name__ == "__main__":
    solve()