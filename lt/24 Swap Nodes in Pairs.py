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
    def swapPairs(self, head):
        if not head:
            return
        if not head.next:
            return head
        slow = head
        fast = head.next
        cun = head
        cun1 = fast
        while cun and slow and fast:
            cun = fast.next
            fast.next = slow
            if cun:
                if cun.next:
                    slow.next = cun.next
                else:
                    slow.next = cun
            else:
                slow.next = cun
            if cun:
                slow = cun
                fast = cun.next
        return cun1
head = construct([1,2,3,4])
print(printlistnode(head))
print(printlistnode(Solution().swapPairs(head)))
