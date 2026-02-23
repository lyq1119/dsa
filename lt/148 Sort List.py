# Definition for singly-linked list.
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
    def sortList(self, head):
        if not head:
            return head
        mylist = printlistnode(head)
        mylist.sort()
        return construct(mylist)
print(*printlistnode(Solution().sortList(construct([-1,5,3,4,0]))))
        
        