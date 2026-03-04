class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        mydict = {}
        def dfs(node,s):
            if node.left:
                dfs(node.left,s+"0")
            if node.right:
                dfs(node.right,s+"1")
            mydict[node] = s
        dfs(root,"0")
        p1 = mydict[p]
        q1 = mydict[q]
        j = 0
        for i in range(min(len(p1),len(q1))):
            if p1[i] == q1[i]:
                j = i
        s = p1[:(j+1)]
        node = root
        for i in range(1,j+1):
            t = s[i]
            if t == "0":
                node = node.left
            else:
                node = node.right
        return node