import sys
data = list(map(int,sys.stdin.read().split()))
class Binaryheap:
    def __init__(self,mylist):
        self.heap = mylist
    def exchange(self,i):
        if not self.heap:
            return
        m = self.heap[i-1]
        if 2*i+1 <= len(self.heap) and m < max(self.heap[2*i],self.heap[2*i-1]):
            if self.heap[2*i] >= self.heap[2*i-1]:
                self.heap[i-1],self.heap[2*i] = self.heap[2*i],self.heap[i-1]
                self.exchange(2*i+1)
            else:
                self.heap[i-1],self.heap[2*i-1] = self.heap[2*i-1],self.heap[i-1]
                self.exchange(2*i)
        elif 2*i == len(self.heap) and m < self.heap[2*i-1]:
            self.heap[i-1],self.heap[2*i-1] = self.heap[2*i-1],self.heap[i-1]
            self.exchange(2*i)
n = data[0]
heapq = Binaryheap(data[1:])
for i in range(n,0,-1):
    heapq.exchange(i)
print(*heapq.heap)


    
    