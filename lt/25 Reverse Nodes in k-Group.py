class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        if not head:
            return head
        if k == 1:
            return head
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        cur.next = ListNode(length+1) 
        lh = head
        numpy = ListNode(0)
        numpy.next = head
        curwei = numpy
        for _ in range(length//k):
            wei = lh
            nxt = lh.next
            for __ in range(k-1):   
                xinnxt = nxt.next
                nxt.next = lh
                lh = nxt
                nxt = xinnxt
            curwei.next = lh
            curwei = wei
            wei.next = nxt
            lh = nxt
        while wei.next.next:
            wei = wei.next
        wei.next = None
        return numpy.next
def construct(mylist):
    head = ListNode()
    cur = head
    for num in mylist:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next
def show(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
newhead = Solution().reverseKGroup(construct([1,2,3,4,5]),2)
print(show(newhead))




        