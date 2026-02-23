class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
import math
import sys
mylist = sys.stdin.read()
n = len(mylist)
cur = [0]
def construct():
    if mylist[cur[0]] == ".":
        cur[0] += 1
        return
    tree = TreeNode(mylist[cur[0]])
    cur[0] += 1
    tree.left = construct()
    tree.right = construct()
    return tree
result = []
def zhongxu_traversal(node):
    if node:
        zhongxu_traversal(node.left)
        result.append(node.val)
        zhongxu_traversal(node.right)
result1 = []
def houxu_traversal(node):
    if node:
        houxu_traversal(node.left)
        houxu_traversal(node.right)
        result1.append(node.val)
tree = construct()
zhongxu_traversal(tree)
houxu_traversal(tree)
print("".join(result))
print("".join(result1))