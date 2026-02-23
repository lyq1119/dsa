class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
import math
mylist = [3,1,4,None,2]
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
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        mylist = []
        def zhongxu(root):
            if root:
                zhongxu(root.left)
                mylist.append(root.val)
                zhongxu(root.right)
        zhongxu(root)
        return mylist[k-1]
print(Solution().kthSmallest(constructtree(0,1),1))
        