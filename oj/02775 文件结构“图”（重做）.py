import sys
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.dir = []
        self.file = []
    def __lt__(self, other):
        return self.val < other.val

def solve(t,i,data):
    print(f"DATA SET {i}:")
    root = TreeNode("ROOT")
    stack = [root]
    for m in range(t,len(data)):
        s = data[m]
        if s == "*":
            break
        if s == "]":
            stack.pop()
        elif s[0] == "f":
            s = TreeNode(s)
            stack[-1].file.append(s)
        elif s[0] == "d":
            s = TreeNode(s)
            stack[-1].dir.append(s)
            stack.append(s)
    def dfs(node,ceng):
        if node:
            print("|     "*ceng+node.val)
            for dir in node.dir:
                dfs(dir,ceng+1)
            for file in sorted(node.file):
                dfs(file,ceng)
    dfs(root,0)
    return m+1

data = sys.stdin.read().split()
n = len(data)
mylist = []
i = 0
t = 0
while t < n-1:
    i += 1
    j = solve(t,i,data)
    t = j
    if t != n-1:
        print("")
