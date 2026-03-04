# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        if not root:
            return 0
        mydict = {root:[targetSum]}
        count = 0
        def dfs(node):
            nonlocal count
            count += mydict[node].count(node.val)
            myset = [targetSum]
            for num in mydict[node]:
                myset.append(num - node.val)
            if node.left:
                mydict[node.left] = myset
                dfs(node.left)
            if node.right:
                mydict[node.right] = myset
                dfs(node.right)
        dfs(root)
        return count