class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def genduanpath(node):
    if not node:
        return 0
    return max(max(genduanpath(node.left),genduanpath(node.right))+node.val,0)
def findmax(node):
    if not node:
        return 0
    a = genduanpath(node.left)
    b = genduanpath(node.right)
    return max([node.val+a,node.val+b,node.val,node.val+a+b,a,b,findmax(node.left),findmax(node.right)])
class Solution:
    def maxPathSum(self, root) -> int:
        rootyuansu = []
        def preorder(root):
            if root:
                rootyuansu.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        a = max(rootyuansu)
        if a >= 0:
            return findmax(root)
        return a