class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def lowbit(self, x):
        return x & -x
    def update(self, i, delta):
        """将第 i 个元素增加 delta"""
        while i <= self.size:
            self.tree[i] += delta
            i += self.lowbit(i)
    def query(self, i):
        """查询前 i 个元素的和"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= self.lowbit(i)
        return s
    
n = int(input())
stocks = []
for _ in range(n):
    stocks.append(int(input()))

mylist1 = [n-1 for _ in range(n)]
stack = []
for i in range(n):
    while stack and stocks[i] <= stocks[stack[-1]]:
        mylist1[stack.pop()] = i-1
    stack.append(i)
stack = []
mylist2 = [0 for _ in range(n)]
countlist = [[] for _ in range(n)]
for i in range(n-1,-1, -1):
    while stack and stocks[i] >= stocks[stack[-1]]:
        t= stack.pop()
        mylist2[t] = i+1
        countlist[i+1].append(t)
    stack.append(i)
for i in range(n):
    if mylist2[i] == 0:
        countlist[0].append(i)
tree = BIT(n)
maxlength = 0
for i in range(n):
    for t in countlist[i]:
        tree.update(t+1, 1)
    a = tree.query(mylist1[i]+1)
    if a == 0:
        continue
    left,right = i+1,mylist1[i]+1
    if left == right:
        continue
    while left < right:
        mid = (left + right) // 2
        if tree.query(mid) == a:
            right = mid
        else:
            left = mid
        if left == right - 1:
            if tree.query(right) == a:
                maxlength = max(maxlength, right-i)
            else:
                maxlength = max(maxlength, right-i+1)
            break
print(maxlength)
