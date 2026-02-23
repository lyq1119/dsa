class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def invertTree(self, root):
        def invert(root):
            if not root:
                return root
            a = invert(root.right)
            b = invert(root.left)
            root.left = a
            root.right = b
            return root
        return invert(root)
mylist = [4,2,7,1,3,6,9]
cengshu = int(math.log2(len(mylist)+1))-1
def constructtree(ceng,k):#层序，第ceng层的第k个，根在第0层
    if ceng > cengshu:
        return
    m = (1 << ceng)+k-2
    if not mylist[m]:
        return
    node = TreeNode(mylist[m])
    node.left = constructtree(ceng+1,2*k-1)
    node.right = constructtree(ceng+1,2*k)
    return node
result = []
def preorder_traversal(node):
    if node:
        result.append(node.val)
        preorder_traversal(node.left)
        preorder_traversal(node.right)
tree = constructtree(0,1)
tree1 = Solution().invertTree(tree)
preorder_traversal(tree1)
print(*result)