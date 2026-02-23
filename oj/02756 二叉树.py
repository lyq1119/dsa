visited = set()
m,n = map(int,input().split())
while m:
    visited.add(m)
    m //= 2
while n:
    if n in visited:
        print(n)
        break
    n //= 2