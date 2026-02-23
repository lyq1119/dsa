class ListNode:
    def __init__(self,val=-1,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
def show(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(*result)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mydict = {}
        self.mydict1 = {}
        self.node = ListNode()
        self.diu = self.node
    def get(self, key: int) -> int:
        if key in self.mydict:
            value = self.mydict[key].val
            node = ListNode(value)
            self.node.next = node
            node.prev = self.node
            self.node = node
            cur = self.mydict[key]
            self.mydict[key] = node
            del self.mydict1[cur]
            self.mydict1[node] = key
            if cur != self.diu:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            else:
                self.diu = self.diu.next
            show(self.diu)
            return value
        else:
            show(self.diu)
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.mydict:
            node = ListNode(value)
            self.node.next = node
            node.prev = self.node
            self.node = node
            cur = self.mydict[key]
            self.mydict[key] = node
            del self.mydict1[cur]
            self.mydict1[node] = key
            if cur != self.diu:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            else:
                self.diu = self.diu.next
        else:
            if len(self.mydict) == self.capacity:
                key1 = self.mydict1[self.diu]
                del self.mydict[key1]
                del self.mydict1[self.diu]
                node = ListNode(value)
                self.node.next = node
                node.prev = self.node
                self.node = node
                self.mydict[key] = node
                self.mydict1[node] = key
                self.diu = self.diu.next
            else:
                node = ListNode(value)
                self.node.next = node
                node.prev = self.node
                self.node = node
                self.mydict[key] = node
                self.mydict1[node] = key
                if self.diu.val == -1:
                    self.diu = self.diu.next
        show(self.diu)
c = LRUCache(2)
c.put(1,1)
c.put(2,2)
c.get(1)
c.put(3,3)
c.get(2)
c.put(4,4)
c.get(1)
c.get(3)
c.get(4)
