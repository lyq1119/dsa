import sys
sys.setrecursionlimit(300002)
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
for t in range(int(input())):
    n = int(input())
    tree = {i:TreeNode(i) for i in range(n+1)}
    tree[1].parent = tree[0]
    for i in range(1,n+1):
        a,b = map(int,input().split())
        if a == 0 and b == 0:
            continue
        else:
            node = tree[i]
            node.left = tree[a]
            node.right = tree[b]
            tree[a].parent = node
            tree[b].parent = node
    dp = [0]*(n+1)
    def dfs(i):
        node = tree[i]
        if not node.left and not node.right:
            dp[i] = 0
            return 0
        dp[i] = dfs(node.left.val)+dfs(node.right.val)+4
        return dp[i]
    dfs(1)
    mylist = [0]*(1+n)
    visited = [0]*(1+n)
    def dfs1(i):
        if visited[i]:
            return mylist[i]
        visited[i] = 1
        if i == 0:
            return 0
        mylist[i] = (1+dfs1(tree[i].parent.val)+dp[i])%(10**9+7)
        return mylist[i]
    for i in range(n+1):
        dfs1(i)
    print(*mylist[1:])


    