n = int(input())
sequence = []
for i in range(n):
    mylist = list(map(int,input().split()))
    if 0 in mylist:
        s = n-i+1
        mylist.remove(0)
    sequence.extend(mylist) 
shu = [0 for _ in range(n**2)]
def update(i):
    while i < len(shu):
        shu[i] += 1
        i += (i&(-i))
def query(t):
    total = 0
    while t > 0:
        total += shu[t]
        t -= (t&(-t))
    return total
count = 0
for num in sequence:
    num = n**2-num
    count += (query(num)%2)
    count %= 2
    update(num)
if n % 2 == 1:
    if not count:
        print("yes")
    else:
        print("no")
else:
    if (count + s) % 2 == 0:
        print("yes")
    else:
        print("no")