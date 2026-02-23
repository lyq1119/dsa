class BIT:
    def __init__(self,size):
        self.size = size
        self.tree = [0]*size
    def lowbit(self,x):
        return x&(-x)
    def insert(self,i):
        a = self.query(i-1)
        while i <= self.size:
            self.tree[i-1] += 1
            i += self.lowbit(i)
        return a
    def query(self,i):
        total = 0
        while i:
            total += self.tree[i-1]
            i -= self.lowbit(i)
        return total
N = int(input())
mylist = []
for _ in range(N):
    mylist.append(int(input()))
bit = BIT(max(mylist))
total1 = 0
for num in mylist:
    total1 += bit.insert(num)
print(total1)