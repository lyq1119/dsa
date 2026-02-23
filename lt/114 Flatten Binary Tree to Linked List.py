# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def flat(node):
            if not node:      
                return
            a = node
            b = node.right
            node.right = flat(node.left)
            node.left = None
            while node.right:
                node = node.right
            node.right = flat(b) 
            return a
        flat(root)