import sys
data = iter(sys.stdin.read().split())
class Binaryheap:
    def __init__(self):
        self.heap = []
    def insert(self,i):
        self.heap.append(i)
        cur = len(self.heap)
        while cur != 1:
            cur1 = cur//2
            if self.heap[cur1-1] > i:
                self.heap[cur1-1],self.heap[cur-1] = self.heap[cur-1],self.heap[cur1-1]
                cur = cur1
            else:
                break
    def exchange(self,i):
        if not self.heap:
            return
        m = self.heap[i-1]
        if 2*i+1 <= len(self.heap) and m > min(self.heap[2*i],self.heap[2*i-1]):
            if self.heap[2*i] <= self.heap[2*i-1]:
                self.heap[i-1],self.heap[2*i] = self.heap[2*i],self.heap[i-1]
                self.exchange(2*i+1)
            else:
                self.heap[i-1],self.heap[2*i-1] = self.heap[2*i-1],self.heap[i-1]
                self.exchange(2*i)
        elif 2*i == len(self.heap) and m > self.heap[2*i-1]:
            self.heap[i-1],self.heap[2*i-1] = self.heap[2*i-1],self.heap[i-1]
            self.exchange(2*i)
    def delete(self):
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        a = self.heap.pop()
        self.exchange(1)
        return a
heapq = Binaryheap()
for _ in range(int(next(data))):
    a = next(data)
    if a == "1":
        b = int(next(data))
        heapq.insert(b)
    else:
        print(heapq.delete())
        