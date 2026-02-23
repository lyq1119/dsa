import sys
mystr = sys.stdin.read().split()
#Part1 转后序表达式
stack = []
houxubolanbiaodashi = []
for s in mystr:
    if s == "(":
        stack.append(s)
    elif s == "not":
        while stack and stack[-1] == "not":
            houxubolanbiaodashi.append(stack.pop())
        stack.append(s)
    elif s == "and":
        while stack and (stack[-1] == "not" or stack[-1] == "and"):
            houxubolanbiaodashi.append(stack.pop())
        stack.append(s)
    elif s == "or":
        while stack and (stack[-1] == "not" or stack[-1] == "and" or stack == "or"):
            houxubolanbiaodashi.append(stack.pop())
        stack.append(s)
    elif s == ")":
        while stack and stack[-1] != "(":
            houxubolanbiaodashi.append(stack.pop())
        stack.pop()
    else:
        houxubolanbiaodashi.append(s)
while stack:
    houxubolanbiaodashi.append(stack.pop())
#Part2 后序表达式转树
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
stack = []
for s in houxubolanbiaodashi:
    if s == "or" or s == "and":
        node = TreeNode(s)
        node.right = stack.pop()
        node.left = stack.pop()
        stack.append(node)
    elif s == "not":
        node = TreeNode(s)
        node.right = stack.pop()
        stack.append(node)
    else:
        node = TreeNode(s)
        stack.append(node)
tree = stack[0]
#Part3 从树还原出带括号的中序表达式
result = []
def zhongxu(node):
    if node.val == "not":
        result.append(node.val)
        a = node.right
        if not a:
            return
        if a.val == "or" or a.val == "not" or a.val == "and":
            result.append("(")
            zhongxu(a)
            result.append(")")
        else:
            zhongxu(a)
    elif node.val == "and":
        a = node.left
        b = node.right
        if a.val == "or":
            result.append("(")
            zhongxu(a)
            result.append(")")
        else:
            zhongxu(a)
        result.append(node.val)
        if b.val == "or" or b.val == "and":
            result.append("(")
            zhongxu(b)
            result.append(")")
        else:
            zhongxu(b)
    elif node.val == "or":
        a = node.left
        b = node.right
        zhongxu(a)
        result.append(node.val)
        if b.val == "or":
            result.append("(")
            zhongxu(b)
            result.append(")")
        else:
            zhongxu(b)
    else:
        result.append(node.val)
zhongxu(tree)
print(*result)