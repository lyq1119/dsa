# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
mylist = [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None]
cengshu = int(math.log2(len(mylist)+1))-1
def constructtree(ceng,k):#层序，第ceng层的第k个，根在第0层
    if ceng > cengshu:
        return
    m = (1 << ceng)+k-2
    if mylist[m] != 0 and not mylist[m]:
        return
    node = TreeNode(mylist[m])
    node.left = constructtree(ceng+1,2*k-1)
    node.right = constructtree(ceng+1,2*k)
    return node
root = constructtree(0,1)
result = []
def preorder_traversal(node):
    if node:
        result.append(node.val)
        preorder_traversal(node.left)
        preorder_traversal(node.right)
preorder_traversal(root)
print(*result)
from collections import defaultdict
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        mydict = defaultdict(list)
        def dfs(node,depth,path):
            nonlocal max_depth
            max_depth = max(max_depth,depth)
            if not node.left and not node.right:
                if depth == max_depth:
                    mydict[depth].append(path.copy())
                    return
            if node.left:
                dfs(node.left,depth+1,path+[node.left]) 
            if node.right:
                dfs(node.right,depth+1,path+[node.right])
        dfs(root,0,[root])
        for _ in range(max_depth+1):
            myset = set()
            for path in mydict[max_depth]:
                myset.add(path.pop())
            if len(myset) == 1:
                return next(iter(myset))
print(Solution().lcaDeepestLeaves(root))