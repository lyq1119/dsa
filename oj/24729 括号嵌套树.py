import sys
mystr = sys.stdin.read()
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = []
stack = []
for s in mystr:
    if s.isalpha():
        stack.append(TreeNode(s))
    elif s == ")":
        children = []
        while True:
            a = stack.pop()
            if a == "(":
                break
            if a == ",":
                continue
            children.append(a)
        stack[-1].children.extend(children)
    else:
        stack.append(s)
tree = stack[0]
result = []
def qianxu(root):
    if root:
        result.append(root.val)
        for node in reversed(root.children):
            qianxu(node)
result1 = []
def houxu(root):
    if root:
        for node in reversed(root.children):
            houxu(node)
        result1.append(root.val)
qianxu(tree)
houxu(tree)
print("".join(result))
print("".join(result1))