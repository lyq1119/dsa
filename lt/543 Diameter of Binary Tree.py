class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def checkheight(node):
            if not node:
                return -1
            return max(checkheight(node.left),checkheight(node.right))+1
        def checkd(node):
            if not node:
                return -1
            if node:
                return max(2+checkheight(node.left)+checkheight(node.right),max(checkd(node.left),checkd(node.right)))
        return checkd(root)