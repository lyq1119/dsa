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
def show(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
import heapq
class Solution:
    def mergeKLists(self, lists):
        mylist = []
        numpy = ListNode()
        cur = numpy
        for i,Ll in enumerate(lists):
            if Ll:
                heapq.heappush(mylist,(Ll.val,i,Ll))
        while mylist:
            val,j,l = heapq.heappop(mylist)
            cur.next = ListNode(val)
            cur = cur.next
            l = l.next
            if l:
                heapq.heappush(mylist,(l.val,j,l))
        return numpy.next
        
lists = [construct([1,4,5]),construct([1,3,4]),construct([2,6])]
print(show(Solution().mergeKLists(lists)))