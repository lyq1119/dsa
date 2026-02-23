import sys
from collections import defaultdict
data = sys.stdin.readlines()
n = int(data[0][:-1])
mydict = defaultdict(list)
jiedianzhi = set()
feigenjiedianzhi = set()
for i in range(1,n+1):
    mylist = data[i][:-1].split()
    jiedianzhi.add(mylist[0])
    for s in mylist[1:]:
        feigenjiedianzhi.add(s)
        mydict[mylist[0]].append(s)
for s in jiedianzhi:
    if s not in feigenjiedianzhi:
        rootzhi = s
        break
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = []
mydict1 = {}
def construct(s):
    tree = TreeNode(s)
    mydict1[int(s)] = tree
    tree.children = [construct(t) for t in mydict[s]]
    return tree
def show(s):
    mylist = [int(t.val) for t in s.children] + [int(s.val)]
    for m in sorted(mylist):
        if m != int(s.val):
            show(mydict1[m])
        else:
            print(s.val)
tree = construct(rootzhi)
show(tree)
