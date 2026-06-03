from typing import List
from collections import defaultdict
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        class TreeNode:
            def __init__(self,val,i):
                self.val = val
                self.index = i
                self.children = set()
                self.num_sub = 1
                self.parent = None

        nodes = [TreeNode(s[i],i) for i in range(len(s))]

        letter = [[] for _ in range(26)]

        for i in range(1,len(parent)):
            nodes[parent[i]].children.add(nodes[i])
            nodes[i].parent = nodes[parent[i]]
        
        stack = []

        def loc(letter):
            return ord(letter)-97

        def dfs2(node):
            """change the tree and return the number of subtree nodes"""
            if not node:
                return 0
            
            if letter[loc(node.val)]:
                node.parent = letter[loc(node.val)][-1]
            
            stack.append(node)
            letter[loc(node.val)].append(node)

            for child in node.children:
                dfs2(child)

            stack.pop()
            letter[loc(node.val)].pop()

        dfs2(nodes[0])
        
        parent = [-1]+[nodes[i].parent.index for i in range(1,len(parent))]
        
        nodes = [TreeNode(s[i],i) for i in range(len(s))]
        for i in range(1,len(parent)):
            nodes[parent[i]].children.add(nodes[i])

        def dfs1(node):
            """return the number of subtree nodes"""
            if not node:
                return 0
            node.num_sub += sum([dfs1(child) for child in node.children])
            return node.num_sub
        
        dfs1(nodes[0])

        return [nodes[i].num_sub for i in range(len(s))]
print(Solution().findSubtreeSizes([-1,0,0,1,1,1],"abaabc"))