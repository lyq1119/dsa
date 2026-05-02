from typing import List
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        class TreeNode:
            def __init__(self,val):
                self.val = val
                self.ru = None
                self.chu = None
                self.children = []
        nodes = [TreeNode(s[i]) for i in range(n)]
        for i,num in enumerate(parent):
            if num == -1:
                continue
            nodes[num].children.append(i)
        curtime = 0
        def dfs(i):
            mystr = ""
            nonlocal curtime
            node = nodes[i]
            node.ru = curtime
            if node.children:
                for pos in sorted(node.children):
                    mystr += dfs(pos)
                    curtime += 1
            mystr += node.val
            node.chu = curtime
            return mystr
        mystr = dfs(0)
        mystr1 = mystr[::-1]
        mylist = [mystr[nodes[i].ru:nodes[i].chu+1] == mystr1[-nodes[i].chu-1:-nodes[i].ru]if nodes[i].ru != 0 else mystr[nodes[i].ru:nodes[i].chu+1] == mystr1[-nodes[i].chu-1:]  for i in range(n) ]
        return mylist
print(Solution().findAnswer([-1,0,0,1,1,2],"aababa"))
