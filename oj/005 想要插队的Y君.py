class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next
class LinkList:
    def __init__(self):
        self.head = None
		
    def initList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def insertCat(self):
            if not self.head:
                self.head = Node(6)
            slow = fast = self.head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            cur = slow.next
            slow.next = Node(6)
            slow.next.next = cur
        
    def printLk(self):
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next
        print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()