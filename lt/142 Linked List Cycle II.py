class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def construct(mylist):
    head = ListNode()
    cur = head
    for num in mylist:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next
def printlistnode(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
class Solution:
    def detectCycle(self, head):
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next