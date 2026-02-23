while True:
    m,n = map(int,input().split())
    visited = set()
    if m == 0 and n == 0:
        break
    i = 0
    count = 0
    while m <= n:
        a = m+(1<<i)-1
        if a <= n:
            count += (1<<i)
        else:
            count += (n-m+1)
        m *= 2
        i += 1
    print(count)