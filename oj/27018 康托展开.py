import sys
data = sys.stdin.read().split()
mod = 998244353
N = int(data[0])
sequence = data[1:]
shu = [0 for _ in range(N+1)]
def update(i):
    while i < len(shu):
        shu[i] += 1
        i += (i&(-i))
def query(t):
    total = 0
    while t > 0:
        total += shu[t]
        t -= (t&(-t))
        total %= mod
    return total
total = 0
product = [1 for _ in range(N+1)]
for i in range(1,N+1):
    product[i] = product[i-1]*i
for i,num in enumerate(sequence):
    num = int(num)
    total += ((num-query(num)-1)*product[N-i-1]%mod)
    total %= mod
    update(num)
total += 1
print(total)