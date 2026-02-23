import sys
rawdata = sys.stdin.read()
data = []
s1 = ""
for s in rawdata:
    if s.isdigit() or s == "-":
        s1 += s
    elif s == " " or s == "\n":
        continue
    else:
        if s1:
            data.append(s1)
        s1 = ""
        data.append(s)
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def solve(mylist,num):
    class Tree:
        def __init__(self):
            self.tree = None
            self.index = 0
            self.count = 0
        def construct(self,node):
            while True:
                a = mylist[self.index]
                self.index += 1
                if a == "(":
                    continue
                if a == ")":
                    return node
                node = TreeNode(int(a))
                node.left = self.construct(node.left)
                node.right = self.construct(node.right)
        def build(self):
            self.tree = self.construct(self.tree)
    tree = Tree()
    tree.build()
    t = tree.tree
    def preorder_traversal(node,cursum):
        cursum += node.val
        if not node.left and not node.right:
            if cursum == num:
                return True
            return False
        if node.left:
            a = preorder_traversal(node.left,cursum)
            if a:
                return True
        if node.right:
            b = preorder_traversal(node.right,cursum)
            if b:
                return True
        return False
    if preorder_traversal(t,0):
        print("yes")
    else:
        print("no")
i = 0
count = 0
while i < len(data):
    if count == 0 and (data[i][0].isdigit() or data[i][0] == "-"):
        num = int(data[i])
        i += 1
        j = i
        continue
    a = data[i]
    i += 1
    if a == "(":
        count += 1
    elif a == ")":
        count -= 1
        if count == 0:
            mylist = data[j:i]
            if mylist == ["(",")"]:
                print("no")
            else:
                solve(mylist,num)