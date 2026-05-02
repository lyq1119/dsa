# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        def dfs(node,path):
            nonlocal total
            if not node.left and not node.right:
                total += int(path)
                return
            if node.left:
                dfs(node.left,path+str(node.left.val))
            if node.right:
                dfs(node.right,path+str(node.right.val))
        dfs(root,str(root.val))
        return total
root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.right = TreeNode(0)
print(Solution().sumNumbers(root))

