import sys
data = sys.stdin.read().split()

def solve():
    for s in data:
        # parse：转后续表达式
        stack = []
        mylist = []
        curnum = ""
        for i in range(len(s)):
            t = s[i]
            if t == "(":
                if curnum:
                    mylist.append((curnum))
                    curnum = ""
                stack.append(t)
            elif t == "+":
                if curnum:
                    mylist.append((curnum))
                    curnum = ""
                while stack and (stack[-1] == "*" or stack[-1] == "+"):
                    mylist.append(stack.pop())
                stack.append(t)
            elif t == "*":
                if curnum:
                    mylist.append((curnum))
                    curnum = ""
                while stack and (stack[-1] == "*"):
                    mylist.append(stack.pop())
                stack.append(t)
            elif t == ")":
                if curnum:
                    mylist.append((curnum))
                    curnum = ""
                while stack and stack[-1] != "(":
                    mylist.append(stack.pop())
                stack.pop()
            else:
                curnum += t
        if curnum:
            mylist.append(curnum)
        while stack:
            mylist.append(stack.pop())
        # 后续表达式建树
        class TreeNode():
            def __init__(self,val):
                self.val = val
                self.left = None
                self.right = None
        stack = []
        for item in mylist:
            if item == "+" or item == "*":
                node = TreeNode(item)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
            else:
                node = TreeNode(item)
                stack.append(node)
        root = stack[0]
        # 树转string
        def construct(root):
            if not root:
                return ""
            s = root.val
            if root.val == "+":
                if root.left:
                    s = construct(root.left)+s
                if root.right:
                    if root.right.val == "+":
                        s += f"({construct(root.right)})"
                    else:
                        s += construct(root.right)
            elif root.val == "*":
                if root.left:
                    if root.left.val == "+":
                        s = f"({construct(root.left)})"+s
                    else:
                        s = construct(root.left) + s
                if root.right:
                    if root.right.val == "+" or root.right.val == "*":
                        s += f"({construct(root.right)})"
                    else:
                        s += construct(root.right)
            return s
        print(construct(root))  

if __name__ == "__main__":
    solve()