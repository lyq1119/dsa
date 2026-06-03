from typing import List
import heapq

class TreeNode:
    def __init__(self,pos):
        self.pos = pos #[x,y]
        self.left = None
        self.right = None
        self.split = 0 #拆分维度，0表示拆x，1表示拆y

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def construct(dim,points):
            '''build a kd-tree, return the current root node'''
            if not points:
                return None
            points.sort(key=lambda x: x[dim])
            mid = len(points)//2
            node = TreeNode(points[mid])
            node.split = dim
            node.left = construct((dim+1)%2,points[:mid])
            node.right = construct((dim+1)%2,points[(mid+1):])
            return node
        
        root = construct(0,points)

        heap = [] #每次弹最大的
        curmax = 0

        def dis(pos):
            return pos[0]*pos[0]+pos[1]*pos[1]

        def search(node):
            '''search a kd-tree and return None'''
            nonlocal curmax

            if not node:
                return
            
            if node.pos[node.split] > 0:
                search(node.left)   
            else:
                search(node.right)

            if len(heap) < k:
                heapq.heappush(heap,(-dis(node.pos),node.pos))
                curmax = max(-heap[0][0],curmax)
            elif len(heap) == k:
                distance =  dis(node.pos)
                if distance < curmax:
                    heapq.heappushpop(heap,(-dis(node.pos),node.pos))
                    curmax = max(-heap[0][0],curmax)
                if node.pos[node.split]**2 >= curmax:
                    return 
                    
            if node.pos[node.split] > 0:
                search(node.right)   
            else:
                search(node.left)
                
        
        search(root)

        return [pair[1] for pair in heap]
    
print(Solution().kClosest([[1,3],[-2,2],[2,-2]],2))