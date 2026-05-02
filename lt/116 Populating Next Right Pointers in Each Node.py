class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from typing import Optional
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        from collections import deque
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node.left:
                    continue
                node.left.next = node.right
                if i >= 1:
                    queue[-1].next = node.left
                queue.append(node.left)
                queue.append(node.right)
        return root