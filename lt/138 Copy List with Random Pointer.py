class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def printlistnode(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
class Solution:
    def copyRandomList(self, head):
        cur = head
        head1 = Node(0)
        cur2 = head1
        length = 0
        mydict = {}
        while cur:
            a = cur.random
            cur1 = head
            k = 0
            while cur1 != a:
                cur1 = cur1.next
                k += 1
            mydict[length] = k
            length += 1
            cur2.next = Node(cur.val)
            cur2 = cur2.next
            cur = cur.next
        head1 = head1.next
        cur = head1
        dijige = 0
        while cur:
            k = mydict[dijige]
            cur1 = head1
            for _ in range(k):
                cur1 = cur1.next
            cur.random = cur1
            dijige += 1
            cur = cur.next
        return head1
        