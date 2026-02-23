import sys
data = iter(list(map(int,sys.stdin.read().split())))
n = next(data)
for i in range(1,n+1):
    print(f"Scenario #{i}:")
    j = next(data)
    k = next(data)
    left,right = 0,0
    while j != 1 or k != 1:
        if j < k:
            if k%j != 0:
                right += k//j
                k %= j
            else:
                right += (k//j)-1
                k = j
        elif k < j:
            if j%k != 0:
                left += j//k
                j %= k
            else:
                left += (j//k)-1
                j = k
    print(left,right)
    if i != n:
        print("")